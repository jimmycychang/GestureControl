import cv2
import time
import HandTrackingModule as htm
import math


wCam, hCam = 640, 480

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc("M","J","P","G"))
pTime = 0

detector = htm.handDetector()

while True:
    success, img = cap.read()
    img = detector.findHands(img, draw=False)
    lmList = detector.findPosition(img)


    if len(lmList) != 0:
        x1, y1 = lmList[4][1], lmList[4][2]
        x2, y2 = lmList[8][1], lmList[8][2]
        cx, cy = (x1+x2)//2, (y1+y2)//2
        cv2.circle(img, (x1,y1), 10, (0,0,255), cv2.FILLED)
        cv2.circle(img, (x2,y2), 10, (0,0,255), cv2.FILLED)
        cv2.line(img, (x1,y1), (x2,y2), (0,0,255),4)
        cv2.rectangle(img, (50,150),(85,400),(0,255,0),cv2.FILLED)

        length = math.hypot(x2-x1, y2-y1)
        lengthhh = round(length)
        
        if lengthhh < 250:
            ratio = round((lengthhh/250)*100,1)
            cv2.rectangle(img, (50,150), (85,400-lengthhh),(255,255,255), cv2.FILLED)
            cv2.putText(img, f'{float(ratio)}%', (40,120), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
            img = cv2.convertScaleAbs(img, alpha=(lengthhh/125), beta=(lengthhh/125))

        else:
            cv2.putText(img, "100%", (40,120), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
            img = cv2.convertScaleAbs(img, alpha=2, beta=2)




    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime


    cv2.putText(img, f'FPS: {int(fps)}', (30,50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 3)
    cv2.imshow("img", img)
    key = cv2.waitKey(1) & 0xFF
    if key==ord('q'):
        break
