import cv2
import numpy as np

img = cv2.imread('C:/Users/valle/Desktop/NIMA_Test/Nima_Test_src.jpg')

kernel = np.ones((10, 10), np.float32)/100
dst = cv2.filter2D(img, -1, kernel)

cv2.imwrite('C:/Users/valle/Desktop/NIMA_Test/Nima_Test_dst.jpg', dst)
