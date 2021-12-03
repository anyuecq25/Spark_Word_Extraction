
from pyspark.sql import SparkSession
#from __future__ import print_function
from pyspark import SparkContext
from pyspark import SparkConf

import numpy as np


import time
#import matplotlib.pyplot as plt
import utils as utils
from pfh import FPFH


"""
only load vertex and faces from .obj model, since we only render depth image
:param path:
:return: model{"pts": np.ndarray, "faces": ndarray}
    """

def load_off(path):
    model = {}
    f = open(path, 'r')
    lines = f.readlines()
    if(len(lines[0].split())>1):
        str=lines[0]
        str=str.replace('OFF','')
        nvertex = int(str.split()[0])
        vt_lines = lines[1:nvertex + 1]
    else:
        nvertex=int(lines[1].split()[0])
        vt_lines=lines[2:nvertex+2]
    vt = np.asarray([l.rstrip().lstrip('v').lstrip().split() for l in vt_lines], dtype=np.float64)
    model['pts'] = vt
    f.close()
    return model

# faces_ = [l.rstrip().lstrip('f').lstrip() for l in lines if l.split(' ')[0] == 'f']
#
# # .obj: face index from 1 while python from 0, so we need to minus 1
# faces = np.asarray([[int(item.split('/')[0])-1 for item in f.split(' ')] for f in faces_], dtype=np.float64)
# model['faces'] = faces


    """
    only load vertex and faces from .obj model, since we only render depth image
    :param path:
    :return: model{"pts": np.ndarray, "faces": ndarray}
    """
def load_obj(path):
    model = {}
    f = open(path, 'r')
    lines = f.readlines()
    vt = np.asarray([l.rstrip().lstrip('v').lstrip().split() for l in lines if l.split(' ')[0]=='v'], dtype=np.float64)
    model['pts'] = vt
    faces_ = [l.rstrip().lstrip('f').lstrip() for l in lines if l.split(' ')[0] == 'f']
    # .obj: face index from 1 while python from 0, so we need to minus 1
    #faces = np.asarray([[int(item.split('/')[0])-1 for item in f.split(' ')] for f in faces_], dtype=np.float64)
    face_array = [[int(item.split('/')[0]) - 1 for item in f.split(' ')] for f in faces_]
    if len(face_array[-1]) == len(face_array[1]):
        faces = np.asarray(face_array, dtype=np.float64)
        model['faces'] = faces
        #model['faces'] = faces
    f.close()
    return model

#import time

#import docx

import numpy as np
import os
import shutil
import random
def read(x,filename,filetype="off"):
    mean_value=np.array([])
    filepath, fullflname = os.path.split(filename)
    prefix = filepath.replace('hdfs://HA/', '')
    prefix = prefix.replace('/', '_')
    docfile = '/dev/shm/' + prefix + fullflname
    #docfile='/dev/shm/'+fullflname
    #print(docfile)
    f_pfh=np.array([])
    try:
        with open(docfile, 'wb') as f:
            f.write(x)
            f.close()
            try:
                if filetype=="off":
                    m = load_off(docfile)
                else:
                    m = load_obj(docfile)
                source_pc_ = m["pts"]

                source_pc = utils.load_pc_obj(source_pc_)

                if len(source_pc)>1000:
                    source_pc = random.sample(source_pc, 1000)

                print("...Done loading point cloud. \n")
                start = time.process_time()
                # Run ICP with some example parameters
                et = 0.1
                div = 2
                nneighbors = 8  # 8
                rad = 0.09  # 0.03
                # Icp = PFH(et, div, nneighbors, rad)   # Full PFH
                # Icp = SPFH(et, div, nneighbors, rad)  # Simplified PFH
                Icp = FPFH(et, div, nneighbors, rad)  # Fast PFH
            except Exception as e:
                print("Exception ", str(e))

            f_pfh = Icp.getFPFH(source_pc)  # cq
            end = time.process_time()
            print("Time (s): ", end - start, "s")

            # if len(source_pc)>0:
            #     mean_value = source_pc_.mean(axis=0)
            # else:
            #     print("source pc is empty",docfile)

            print('call read func once.')


    except Exception:
        a=3
    os.remove(docfile)
    return f_pfh.tolist()

spark_conf = SparkConf()#.setAppName('rdd_read_docx_func_call_testing_115_docs')
#spark_conf = SparkConf().setAppName('rdd_read_docx_no_read_docx')
#spark_conf = SparkConf().setAppName('rdd_read_docx_v4_20cores_7nodes')

    # .setMaster(master)

sc = SparkContext(conf=spark_conf)
#sc.setLogLevel('ERROR')
spark = SparkSession.builder.appName("PythonKMeans").getOrCreate()
total=sc.accumulator(0)

path='datasets/ModelNet40/*/*/*.off'  #ncount=12311
path='datasets/ShapeNetCore.v2/*/*/models/*.obj'  #ncount=52472
#path='datasets/ShapeNetCore.v2/02876657/*/models/*.obj'  #ncount
rdd = sc.binaryFiles(path)

if "off" in path:
    type="off"
else:
    type="obj"

doc=rdd.map(lambda x:(x[0],read(x[1],x[0],type)))


doc_=doc.map(lambda x:[x[0],x[1],len(x[1])])
doc_.cache()
nread=doc_.count()
print("Total model is :",nread)

df=doc_.toDF()

#df.write.parquet('./chenq/3d_model_ModelNet40.parquet')
df.write.parquet('./chenq/3d_model_SahpeNetCore.v2_FPFH_ALL_12cores_16executors_sample1000.parquet')

#df.write.parquet('./chenq/3d_model_SahpeNetCore.v2_FPFH_f186d2998485c6ed5e9e2656aff7dd5b_sample1000.parquet')
sc.stop()