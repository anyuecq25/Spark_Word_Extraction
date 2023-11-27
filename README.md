# Spark_Word_Extraction
This is the project for the Paper 1 and Paper 2. (Paper2 is under review. If you use this code ,please site.)

rdd_read_docx_v_2021_10_11.py    :Reading docx files with Spark, See Algorithm 1 in Paper 1.
#For 3D models:<br>
rdd_read_obj_FPFH.py		 :Extracting FPFH features from 3D models, which is included in Paper2.	

#For images:<br>

step1: python_read_image_compress_to_128M.py  :Extracting image features from images, which is included in Paper2 with compression schema. And each zip file is 128M Byte.

step2: rdd_read_images_tackle_zip_files.py  :Extracting image features from images, which is included in Paper2 with compression schema.	

#bencharmark: for tika<br>
rdd_read_docx_single_node_local_file_shm_with_tika.py : Reading with tika


*.sh is the shell command to run different test for our algorithm.

# Paper1: Qiang Chen*; Yinong; Chen, Sheng Wu, Zili Zhang; <a href='https://ieeexplore.ieee.org/document/9590234' target=_blank>A Spark-based Open Source Framework for Large-Scale Parallel Processing of Rich Text Documents</a>, FiCloud 2021: International Conference on Future Internet of Things and Cloud, Italy, 2021.8.23 (IEEE)

# Paper2. Our extending paper which is submited to Simulation Modelling Practice and Theory.  <br><br>The title is:  A Service-Oriented Framework for Large-Scale Documents Processing and Application via 3D Models and Feature Extraction



2023.11.25


