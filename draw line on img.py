import cv2

img = cv2.imread('assets/logo.jpg',-1)
img = cv2.resize(img, (0,0), fx=0.5, fy=0.5)

dimension = img.shape

height = img.shape[0]
width = img.shape[1]
channels = img.shape[2]

img = cv2.line(img,(0,0), (width, height), (255, 0, 0), 10) #starting posoition, end position, color, line thickness
img = cv2.line(img, (0, height), (width, 0), (0, 255, 0), 5)
img = cv2.rectangle(img, (100,100), (200,200), (128, 128, 128), 5)
img = cv2.circle(img, (300,300), 60, (0,0,255), -1)
font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img, "shefali is great!", (10, height-10), font, 2,  (0, 0, 0), 2, cv2.LINE_AA)



cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()