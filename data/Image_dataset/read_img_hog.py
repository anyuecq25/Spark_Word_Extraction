from skimage.feature import hog
from skimage import io
from PIL import Image
import numpy as np
# import cv2

#im = Image.open('./1_0_0.pgm')
filename='./M001134_12_45_67.5.pgm'
filename='./M002068_27_135_45.pgm'
filename='./M005442_15_45_135.pgm'
filename='./M007376_11_45_45.pgm'
filename='./M008242_33_180_0.pgm'


im = Image.open(filename)
# im=Image.open('./M002068_27_135_45.pgm')
# im=Image.open('./M005442_15_45_135.pgm')
# im=Image.open('./M007376_11_45_45.pgm')
# im=Image.open('./M008242_33_180_0.pgm')

#img = cv2.cvtColor(cv2.imread('./test.jpg'), cv2.COLOR_BGR2GRAY)
print(im.size)
normalised_blocks, hog_image = hog(im, orientations=9, pixels_per_cell=(8, 8), cells_per_block=(8, 8),
                                block_norm='L2-Hys', visualize=True)
#im.show()


img = Image.fromarray(hog_image)
img =img.convert("L")
filename=filename.replace('.pgm','_hog.pgm')
img.save(filename)
#img.show()


#im.show(hog_image)
#cv2.imshow('gray',hog_image)