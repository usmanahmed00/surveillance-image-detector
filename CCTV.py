import cv2

# getting an image
car_img = 'traffic.jpg'

# Our pre-trained car classifier
cascade = 'cars.xml'
cascade2 = 'fullbody.xml'

#img = cv2.imread(car_img)
webcam = cv2.VideoCapture(0)



while True:
    sucfram, frame = webcam.read()

    grayS = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    tracker = cv2.CascadeClassifier(cascade)
    tracker2 = cv2.CascadeClassifier(cascade2)

    detect =  tracker.detectMultiScale(grayS)
    detect2 = tracker2.detectMultiScale(grayS)

    for (x, y, w, h) in detect:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 0, 255), 1)

    for (x, y, w, h) in detect2:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)


    cv2.imshow('The Gahdloot p', frame)
    key = cv2.waitKey(1)
    if key == 81 or key == 113:
        break

webcam.release()
