# -*- coding: utf-8 -*-
""" Car Cascade in Video
Created on Tue Jan 22 14:10:43 2019

@author: Mert
"""

import cv2

cascade_src = 'cars.xml'
video_src = 'video1.avi'

cap = cv2.VideoCapture(video_src)

cars_cascade = cv2.CascadeClassifier(cascade_src)

while True:
    _, img = cap.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    araclar = cars_cascade.detectMultiScale(gray,1.1,1)
    
    for (x,y,w,h) in araclar:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
    cv2.imshow('video',img)
    if cv2.waitKey(25) & 0xFF ==ord('t'): 
        break

cap.release()
cv2.destroyAllWindows()
    
