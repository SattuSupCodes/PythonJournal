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

import cv2 
import numpy as np
import matplotlib as plt

img = cv2.imread("image_processing/images/oh_my_bholenaath.jpeg")
rows, cols = img.shape

pts1 = np.float32([[50, 50],[200,50], [50,200]])
pts2 = np.float32([[10,100], [200,50], [100,250]])
M= cv2.getAffineTransform(pts1,pts2)
dst = cv2.warpAffine(img, M,(cols,rows))
plt.subplot(121), plt.imshow(dst), plt.title('input')
plt.subplot(122), plt.imshow(dst), plt.title('output')
plt.show