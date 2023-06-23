from HandTrackingModule import handDetector
import cv2

wCam, hCam = 640, 480

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

detector = handDetector()

tipIds = [4,8,12,16,20]

while True:
    success, img = cap.read()
    detector.findHands(img, draw=False)
    lmlist = detector.findPosition(img)
    text = ""

    if len(lmlist) != 0:
        thumb1 = lmlist[tipIds[0]][1]
        thumb2 = lmlist[tipIds[0]-1][1]
        index1 = lmlist[tipIds[1]][2]
        index2 = lmlist[tipIds[1]-1][2]
        index3 = lmlist[tipIds[1]-2][2]
        middle1 = lmlist[tipIds[2]][2]
        middle3 = lmlist[tipIds[2]-2][2]
        ring1 = lmlist[tipIds[3]][2]
        ring3 = lmlist[tipIds[3]-2][2]
        pinky1 = lmlist[tipIds[4]][2]
        pinky3 = lmlist[tipIds[4]-2][2]
        
        # number 0~4
        if (thumb1 < thumb2):
            if (index1 > index3) and (middle1 > middle3) and (ring1 > ring3) and (pinky1 > pinky3):
                text = 0            
            if (index1 < index3) and (middle1 > middle3) and (ring1 > ring3) and (pinky1 > pinky3):
                text = 1
            if (index1 < index3) and (middle1 < middle3) and (ring1 > ring3) and (pinky1 > pinky3):
                text = 2
            if (index1 < index3) and (middle1 < middle3) and (ring1 < ring3) and (pinky1 > pinky3):
                text = 3
            if (index1 < index3) and (middle1 < middle3) and (ring1 < ring3) and (pinky1 < pinky3):
                text = 4
        # number 5~9
        if (thumb1 > thumb2):
            if (index1 < index3) and (middle1 < middle3) and (ring1 < ring3) and (pinky1 < pinky3):
                text = 5
            if (index1 > index3) and (middle1 > middle3) and (ring1 > ring3) and (pinky1 < pinky3):
                text = 6
            if (index1 < index3) and (middle1 > middle3) and (ring1 > ring3) and (pinky1 > pinky3):
                text = 7
            if (index1 < index3) and (middle1 < middle3) and (ring1 > ring3) and (pinky1 > pinky3):
                text = 8
            if (index1 < index3) and (middle1 < middle3) and (ring1 < ring3) and (pinky1 > pinky3):
                text = 9
        # special
        if (thumb1 > thumb2) and (index1 > index2) and (middle1 < middle3) and (ring1 < ring3) and (pinky1 < pinky3):
            text = "OK"
        if (thumb1 > thumb2) and (index1 > index3) and (middle1 > middle3) and (ring1 > ring3) and (pinky1 > pinky3):
            text = "Nice"
        if (thumb1 < thumb2) and (index1 < index3) and (middle1 > middle3) and (ring1 > ring3) and (pinky1 < pinky3):
            text = "Rock"
        if (thumb1 > thumb2) and (index1 < index3) and (middle1 > middle3) and (ring1 > ring3) and (pinky1 < pinky3):
            text = "I Love You"
        
        cv2.putText(img, str(text), (45,150), cv2.FONT_HERSHEY_COMPLEX, 3, (0,0,0), 5)

    cv2.imshow("img", img)    
    key = cv2.waitKey(1) & 0xFF
    if key==ord('q'):
        break
