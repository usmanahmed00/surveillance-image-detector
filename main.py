import cv2
from random import randrange

face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# pick an image for detection
img = cv2.imread('Joyner.jpg')

webcam = cv2.VideoCapture(0)


while True:
    sucfram, frame = webcam.read()

    grayfram = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    vidg = face_data.detectMultiScale(grayfram)

    for (x, y, w, h) in vidg:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (randrange(255), randrange(255), randrange(255)), 3)

    cv2.imshow('The Gahdloot p', frame)
    key = cv2.waitKey(1)
    if key == 81 or key ==113:
        break


webcam.release()


'''
# convert to grayscale
BW = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# detecting faces
cordn = face_data.detectMultiScale(BW)

for (x,y,w,h) in cordn:
    cv2.rectangle(img, (x, y), (x+w, y+h), (randrange(255), randrange(255), randrange(255)), 1)


cv2.imshow('The Gahdloot detector', img)
cv2.waitKey()

print('Code has been completed')
'''
