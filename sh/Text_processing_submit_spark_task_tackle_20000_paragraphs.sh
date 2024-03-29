##Submit Spark task for Algorithm 1 and 1.1
#Results shown in Table 3 as 'Improved'
export SPARK_MAJOR_VERSION=2
export SPARK_HOME=/usr/hdp/2.6.1.0-129/spark2

export PYSPARK_DRIVER_PYTHON=/home/ubuntu/env3.5/bin/python3.5
PYSPARK_PYTHON=./VENV/env3.5/bin/python3 
spark-submit --conf spark.yarn.appMasterEnv.PYSPARK_PYTHON=./VENV/env3.5/bin/python3 \
--master yarn-client \
--executor-memory 16g \
--driver-memory 10g \
--executor-cores 16 \
--num-executors 8 \
--name rdd_docx_8_16cores_16G_tackle_20000_paragraphs \
--archives env35.zip#VENV rdd_read_docx_improved_tackle_20000.py
