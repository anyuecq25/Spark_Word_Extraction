# Spark submit script for Algorithm 4.
export SPARK_MAJOR_VERSION=2
export SPARK_HOME=/usr/hdp/2.6.1.0-129/spark2

export PYSPARK_DRIVER_PYTHON=/home/ubuntu/env3.5/bin/python3.5
PYSPARK_PYTHON=./VENV/env3.5/bin/python3 
spark-submit --conf spark.yarn.appMasterEnv.PYSPARK_PYTHON=./VENV/env3.5/bin/python3 \
--master yarn \
--deploy-mode client \
--executor-memory 32g \
--driver-memory 10g \
--conf spark.default.parallelism=40 \
--executor-cores 16 \
--num-executors 8 \
--name read_images_8_20cores_yarn_128M_each_partition \
--archives env35_pillow.zip#VENV rdd_read_images_tackle_zip_files.py
