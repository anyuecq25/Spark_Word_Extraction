#Submit Spark task for Algorithm 1 and 2 without tackling 20000 paragraphs problem.
#Results shown in Table 3 as '1 nodes' etc.
export PYSPARK_DRIVER_PYTHON=/home/ubuntu/env3.5/bin/Python3.5
PYSPARK_PYTHON=./VENV/env3.5/bin/Python3
Spark-submit --conf Spark.yarn.appMasterEnv.PYSPARK_PYTHON=./VENV/env3.5 /bin/Python3 \
--master yarn-client \
--executor-memory 32g \
--driver-memory 10g \
--executor-cores 16 \
--num-executors 4 \
--archives env35.zip#VENV rdd_read_docx.py
