# displaying an image stored in desktop

import cv2 as cv

img = cv.imread("c:/Users/HP/Desktop/wallpaper.jpeg")
cv.imshow("output", img)
cv.waitKey(10000)