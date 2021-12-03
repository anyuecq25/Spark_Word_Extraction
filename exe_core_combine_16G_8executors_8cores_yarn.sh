export SPARK_MAJOR_VERSION=2
export SPARK_HOME=/usr/hdp/2.6.1.0-129/spark2

export PYSPARK_DRIVER_PYTHON=/home/ubuntu/env3.5/bin/python3.5
PYSPARK_PYTHON=./VENV/env3.5/bin/python3 
spark-submit --conf spark.yarn.appMasterEnv.PYSPARK_PYTHON=./VENV/env3.5/bin/python3 \
--master yarn \
--deploy-mode client \
--executor-memory 16g \
--driver-memory 10g \
--executor-cores 8 \
--num-executors 8 \
--name combine_exe_cores_analy_read_docx_16G_8executors_8cores \
--archives env35.zip#VENV rdd_read_docx.py
