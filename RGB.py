import numpy as np
import matplotlib.pyplot as plt
# pip install opencv-python
import cv2
img = cv2.imread('picture/b1.jpg')
b, g, r = cv2.split(img)

pic = np.zeros(np.shape(img), np.uint8)
pic[:, :, 0] = b
cv2.namedWindow('Blue')
cv2.imshow('Blue', pic)
cv2.waitKey(0)

pic = np.zeros(np.shape(img), np.uint8)
pic[:, :, 1] = g
cv2.namedWindow('Green')
cv2.imshow('Green', pic)
cv2.waitKey(0)

pic = np.zeros(np.shape(img), np.uint8)
pic[:, :, 2] = r
cv2.namedWindow('Red')
cv2.imshow('Red', pic)
cv2.waitKey(0)

cv2.destroyAllWindows()