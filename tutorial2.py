import cv2
import numpy as np
import random


img = cv2.imread('assets/logo.jpg',-1) #it takes the pixcel from this image and loads in numpy
print(img)
print(img.shape) #height,width,channels(number of colors red green and blue

# lets find the first row of the image?
print(img[257][45:400])
print(img[257][400])

# #changing the pixcel color?
# for i in range(100):
#     for j in range(img.shape[1]): #rows,columns,channels we want to change the columns?
#         img[i][j] = [random.randint(0,255), random.randint(0,255), random.randint(0,255)]

cv2.imwrite("color_img.jpg", img)





cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

