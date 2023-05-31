import cv2
import numpy as np

img = cv2.resize(cv2.imread('assets/soccer_practice.jpg', 0), (0,0), fx=0.7, fy=0.7) #if you resize your original image you should  resize template img too
template = cv2.resize(cv2.imread('assets/shoe.png', 0), (0,0), fx=0.7, fy=0.7)
h, w = template.shape

methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
            cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED] #methods for template matching?

for method in methods:
    img2 = img.copy()#draw rectangle in duplicate image for each methods
    result = cv2.matchTemplate(img2, template, method) #convolution
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result) #min max value and location in the array
    print(min_loc, max_loc)
    #lets draw rectangle
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        location = min_loc
    else:
        location = max_loc
    bottom_right = (location[0] + w, location[1] + h)
    cv2.rectangle(img2, location, bottom_right, 255, 5)
    cv2.imshow('Match', img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()




#template matching
# 4*4
# 2*2
# W = 4
# w = 2
# H = 4
# h = 2
# (3,3) this is the number of time we can slide thro images
#
# [[255, 255, 255, 255],
#  [255, 255, 255, 255],
#  [255, 255, 255, 255],
#  [255, 255, 255, 255]]
#
# [[255, 255],
# [255, 255]]
# [[1,1,1,1],
#  [1,1,1,1],   #how colosely thy match
#  [1,1,1,1],
#  [1,1,1,1]]