# Spark_Word_Extraction
This is the project for the Paper 1 and Paper 2. (Paper2 is under review. If you use this code ,please site.)

### For text processing(Algorithm 1 and 1.1):<br>
rdd_read_docx.py                          :Original algorithm 2 without tackling 20000 paragraphs problem.
rdd_read_docx_improved_tackle_20000.py    :Improved of reading docx files with Spark, See Algorithm 1, 2  in Paper 1. 

### For compression based text processing(Algorithm 2)<br>
python_read_docx_compress_to_128M.py      :Compressing docx files into Zip file.
rdd_read_docx_tackle_zip_files.py         :Algorithm 2. Compression based text processing.

### For 3D models(Algorithm 3):<br>
rdd_read_obj_FPFH.py		                  :Extracting FPFH features from 3D models, which is included in Paper2.	

### For images(Algorithm 4):<br>

step1: python_read_image_compress_to_128M.py  :Extracting image features from images, which is included in Paper2 with compression schema. And each zip file is 128M Byte.

step2: rdd_read_images_tackle_zip_files.py  :Extracting image features from images, which is included in Paper2 with compression schema.	

### bencharmark: <br>
#For tika<br>
python_read_docx_tika.py : Reading with tika on local machine.
#For python-docx:<br>
python_read_docx.py   : Serial algorithm of Python-docx running on local machine.
<br>
### sh/*.<br>
sh is the shell command to run different test for our algorithm.

#Paper1: Qiang Chen*; Yinong; Chen, Sheng Wu, Zili Zhang; <a href='https://ieeexplore.ieee.org/document/9590234' target=_blank>A Spark-based Open Source Framework for Large-Scale Parallel Processing of Rich Text Documents</a>, FiCloud 2021: International Conference on Future Internet of Things and Cloud, Italy, 2021.8.23 (IEEE)

#Paper2. Our extending paper which is submited to Simulation Modelling Practice and Theory.  <br><br>The title is:  A Service-Oriented Framework for Large-Scale Documents Processing and Application via 3D Models and Feature Extraction



Nov. 25 2023

