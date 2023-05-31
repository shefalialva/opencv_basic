import cv2
import numpy as np
import random

img = cv2.imread('assets/logo.jpg',-1)
tag = img[500:700, 600:900] #i will copy rows from 500 to 700 and the columns from 600 to 500 in the row
img[100:300, 650:950] = tag  #this should be same dimention as tag



cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()