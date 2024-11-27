import cv2 
import numpy as np

img = cv2.imread("C:/Users/HP/Desktop/LearnPython/Image_Processing/images/oh_my_bholenaath.jpeg",0)
rows , cols = img.shape 
M = cv2.getRotationMatrix2D((cols/2, rows/2), 90,1)
dst = cv2.warpAffine(img, M, (cols, rows))

cv2.imshow("original image", img)
cv2.imshow("rotated image" , dst)

cv2.waitKey(0)
cv2.destroyAllWindows()