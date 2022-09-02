from operator import imod
from tkinter.tix import Tree


import cv2

face_cascades = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# ЭТО кусок для распознавания лица на фотке, картинке
# img = cv2.imread("face.jpeg")
# img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# faces = face_cascades.detectMultiScale(img_gray)

# for (x, y, w, h) in faces:
#     cv2.rectangle(img, (x,y), (x + w, y + h), (255,0,0), 1)

# cv2.imshow('Result', img)
# cv2.waitKey(0)

# ЭТО кусок для распознавания лица в видеокамере
cap = cv2.VideoCapture(0)

while True:
    success, frame = cap.read()
    img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascades.detectMultiScale(img_gray)
    
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x,y), (x + w, y + h), (255,255,0), 1)
    
    cv2.imshow('Result', frame)
    
    if cv2.waitKey(1) & 0xff == ord("q"):
        break
    