import cv2
import HandTrackingModule as htm
import math
import numpy as np


wCam, hCam = 640, 480

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
pTime = 0

detector = htm.handDetector()

while True:
    success, img = cap.read()

    img = detector.findHands(img, draw=False)
    lmList = detector.findPosition(img)
    state = "normal"


    if len(lmList) != 0:
        x1, y1 = lmList[4][1], lmList[4][2]
        x2, y2 = lmList[8][1], lmList[8][2]
        cx, cy = (x1+x2)//2, (y1+y2)//2
        cv2.circle(img, (x1,y1), 10, (255,0,0), cv2.FILLED)
        cv2.circle(img, (x2,y2), 10, (255,0,0), cv2.FILLED)
        cv2.line(img, (x1,y1), (x2,y2), (255,0,0),4)

        length = math.hypot(x2-x1, y2-y1)
        lengthhh = np.interp(length,(30,160), (0,100))
        bar = np.interp(length,(30,160), (400,150))

        light1 = np.interp(length, (30,93), (0,100))
        light2 = np.interp(length, (97,160), (0,100))

        if 49 <= lengthhh <= 51:
            img = img
            state = "normal"
        elif lengthhh < 49:
            img = cv2.convertScaleAbs(img, alpha=(light1/100), beta=(light1/100))
            state = "dark"
        else:
            img = cv2.convertScaleAbs(img, alpha=(light2/100)+1, beta=(light2/100))
            state = "bright"

       
        cv2.rectangle(img, (50,150), (85,400),(0,255,0), 3)
        cv2.rectangle(img, (50,int(bar)), (85,400),(0,255,0), cv2.FILLED)
        cv2.putText(img, f'{int(lengthhh)}%', (40,120), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

    cv2.putText(img, f'{str(state)}', (150,120), cv2.FONT_HERSHEY_PLAIN, 3, (0,255,0), 2)

    cv2.imshow("Brightness Adjust", img)
    key = cv2.waitKey(1) & 0xFF
    if key==ord('q'):
        break
