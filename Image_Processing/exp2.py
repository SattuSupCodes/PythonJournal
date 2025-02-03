# transforming between images and methods for computing them

# a Wrap affine tranformation

import cv2 
import numpy as np

img = cv2.imread("image_processing/images/oh_my_bholenaath.jpeg",0)

rows, cols = img.shape

M = np.float32([[1,0,100], [0,1,50]])

dst = cv2.warpAffine(img,M,(cols,rows))

cv2.imshow('img', dst)
cv2.waitKey(0)

cv2.destroyAllWindows()

# Affine transformation

