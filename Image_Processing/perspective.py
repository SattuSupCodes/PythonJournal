import cv2 as cv
import numpy as np
import matplotlib as plt

img = cv.imread("C:/Users/HP/Desktop/LearnPython/Image_Processing/images/oh_my_bholenaath.jpeg")

rows, cols, ch = img.shape

pts1 = np.float32