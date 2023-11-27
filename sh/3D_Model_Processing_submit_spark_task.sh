#3D processing, need another two file. pfh.py and utils.py 
export SPARK_MAJOR_VERSION=2
export SPARK_HOME=/usr/hdp/2.6.1.0-129/spark2

export PYSPARK_DRIVER_PYTHON=/home/ubuntu/env3.5/bin/python3.5
PYSPARK_PYTHON=./VENV/env3.5/bin/python3 
spark-submit --conf spark.yarn.appMasterEnv.PYSPARK_PYTHON=./VENV/env3.5/bin/python3 \
--master yarn \
--deploy-mode client \
--executor-memory 8g \
--driver-memory 10g \
--executor-cores 12 \
--num-executors 16 \
--name read_3d_model_fpfh_12G_12cores_16executors \
--conf spark.default.parallelism=40 \
--conf spark.files.maxPartitionBytes=2097152 \
--py-files pfh.py,utils.py \
--archives env35_fpfh.zip#VENV rdd_read_obj_FPFH.py
