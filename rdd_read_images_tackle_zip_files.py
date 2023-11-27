#Extracting image features from images. Nov.25 2023
from pyspark.sql import SparkSession

#from __future__ import print_function

from pyspark import SparkContext
from pyspark import SparkConf

import os

#PYSPARK_PYTHON = "/home/ubuntu/env3.5/bin/python3.5"
#os.environ["PYSPARK_PYTHON"] = PYSPARK_PYTHON



from pyspark.ml.feature import HashingTF,IDF,Tokenizer



#spark_conf = SparkConf().setAppName('rdd_read_docx_6_nodes_store_tmp_20cores_16G_tackle_word_cannot_read_problem')
spark_conf = SparkConf()#.setAppName('rdd_read_docx_func_call_testing_115_docs')
#spark_conf = SparkConf().setAppName('rdd_read_docx_no_read_docx')
#spark_conf = SparkConf().setAppName('rdd_read_docx_v4_20cores_7nodes')

    # .setMaster(master)

sc = SparkContext(conf=spark_conf)
#sc.setLogLevel('ERROR')
spark = SparkSession.builder.appName("PythonKMeans").getOrCreate()

total=sc.accumulator(0)

import sys
import time
def get_text_from_docx(input_docx_path):
	start = time.clock()
	docs = docx.Document(input_docx_path)
	text_list=[]
	n_p =len(docs.paragraphs)
	if (n_p > 2000):
		res = 'paragraph count >2000'
		print(input_docx_path+' paragraph count >2000  is: '+str(n_p))
		return res
	for i in range(n_p):
		string_=docs.paragraphs[i].text
		if string_ != ' ' and string_ != ' ' and len(string_) > 0:
			text_list.append(string_.strip())
	for table in docs.tables:
	    for row in table.rows:
	        for cell in row.cells:
	            text_list.append(cell.text.strip())   # new method faster than before 190s->24s by qchen 2021.2.7
	duration=int((time.clock() - start))
	if duration>1:
		print(input_docx_path+' , execution time:\t' + str(duration) + 's')
	return " ".join(text_list)


import os
#import docx
import shutil
#from PIL import Image
#import cv2
from skimage.feature import hog

from skimage import io as skio
def processing_files_hog(filename):   # Extract HOG feature, as shown in Algorithm 4. Nov.26 2023
	filepath, fullflname = os.path.split(filename)
	docfile = '/dev/shm/' + filename 	#docfile=filename
	res=""
	try:
		#im = Image.open(docfile)
		#res = im.size
		#img = cv2.imread('./001.pgm')
		#res = img.shape

		img = skio.imread(docfile)  # Read file
		normalised_blocks, hog_image = hog(img, orientations=9, pixels_per_cell=(8, 8), cells_per_block=(8, 8),
												block_norm='L2-Hys', visualize=True) #Extract HOG feature
		res=hog_image
	except Exception as e:
		print('exception: '+str(e))
	os.remove(docfile)
	print(fullflname+' *optimized table reading in zip * file length :' + str(res))
	return res


import io
import zipfile
def itemsToRow(content,filename):
	filelist=[]
	itemlist = []
	f = zipfile.ZipFile(io.BytesIO(content))
	for file in f.namelist():  # f.namelist() Returned value is a List. Each element of the list corresponds to each file in the compressed file.
		f.extract(file, "/dev/shm/")
		#print('this is the zip files '+file)
		filelist.append(file)
		res=processing_files_hog(file)
		newrow=(file,res)
		itemlist.append(newrow)
	return itemlist


def read_image_size(x,filename):   #Only get the image size, do not etract image feature. Resutls shown in Table9 -'Get Image Size' 2023.11.25
	#return ""
	filepath, fullflname = os.path.split(filename)
	prefix = filepath.replace('hdfs://HA/', '')
	prefix = prefix.replace('/', '_')

	docfile = '/dev/shm/' + prefix + fullflname
	#docfile = '/tmp/' + fullflname
	res=""
	try:
		with open(docfile, 'wb') as f:
			f.write(x)
			f.close()
			#docs = docx.Document('/tmp/'+filename)
			try:
				#res=get_text_from_docx(docfile)
				im = Image.open(docfile)
				res=im.size
				#print(docfile)
				#print('call read func once.')
				#print('1')
				#with open(docfile+'_tmp','w') as t:
				#	t.write("")
				#	t.close()
			except Exception:
				a=2
	except Exception:
		a=3

	#import shutil
	tmp_path=docfile
	os.remove(docfile)
	return res

path='file:///home/ubuntu/chenq/docx_evaluate_score/data/all_docx/input/*.docx'
path='file:///home/ubuntu/chenq/test_docx/input/*.docx'
path='file:////dev/shm/input/*.docx'
path='file:////dev/shm/input2/input/*.docx'
path='/user/ubuntu/docx/input/*.docx'
path='/user/ubuntu/test_docx/input/*.docx'  #20201119   ncount=10345
path='/user/ubuntu/chenq/all_docx/input/*.docx'  #20201119   ncount=175420

#export PYSPARK_DRIVER_PYTHON=/home/ubuntu/env3.5/bin/python3.5
#PYSPARK_PYTHON=/home/ubuntu/env3.5/bin/python3.5
#pyspark --master local[12] --executor-memory 32g --driver-memory 10g

# Here is the main_procedure show in Algorithm 1, Algorithm 4.   Updated by Nov.26 2023
path='./chenq/Projection_Shrec14_Zip_128M/a*1.zip' # zip files ,almost 1.2G
rdd = sc.binaryFiles(path)
doc=rdd.flatMap(lambda x:itemsToRow(x[1],x[0]))
#doc.cache()
#nread=doc.count()
#print(nread)

df=doc.toDF()
df.cache()
nread=df.count()
print(nread)
import time
ticks = time.time()
saved_parquet_name='./mini_zip_docx/mini_zip_docx_'+str(int(ticks))+'.parquet'
print('saved_parquet_name :'+saved_parquet_name)
#df.write.parquet(saved_parquet_name)

sc.stop()
'''
while(nread>0):
	rdd1 = sc.binaryFiles(path)
	doc1 = rdd1.map(lambda x: (x[0], read(x[1], x[0])))
	nread = doc1.count()
	if(nread>0):
		doc=doc.union(doc1)
		print('This time read: '+str(nread))

print('total count is:'+str(doc.count()))
#print(doc.first()[0])
#print(doc.first()[1])
'''





