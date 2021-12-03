export SPARK_MAJOR_VERSION=2
export SPARK_HOME=/usr/hdp/2.6.1.0-129/spark2

export PYSPARK_DRIVER_PYTHON=/home/ubuntu/env3.5/bin/python3.5
PYSPARK_PYTHON=./VENV/env3.5/bin/python3 
spark-submit --conf spark.yarn.appMasterEnv.PYSPARK_PYTHON=./VENV/env3.5/bin/python3 \
--master yarn \
--deploy-mode client \
--executor-memory 4g \
--driver-memory 10g \
--executor-cores 2 \
--num-executors 64 \
--name combine_exe_cores_analy_read_docx_4G_64executors_2cores \
--archives env35.zip#VENV rdd_read_docx.py
