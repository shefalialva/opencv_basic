# its pre trained classfier it will look at the imageand try to pick of specific image,
# this classfiers are trained on thousand of images and they determin which feature makes up the face and eye etc
# each classfier has his own task , is train on specific feature, just eye, just face etc
import cv2
import numpy as np

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')


while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5) #this will detect the face , 1.3 is how much of the image we show shrink , 1.5 is recommeded
    for (x, y, w, h) in faces: #as it is giving me rectangle so we are taking x, y , w,h
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 5)
        roi_gray = gray[y:y + w, x:x + w] #this will crop the image buy using region of intrest on gray image
        roi_color = frame[y:y + h, x:x + w] #this will crop the image buy using region of intrest on color image
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.3, 5)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 5)

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cap.detroyAllWindows()

