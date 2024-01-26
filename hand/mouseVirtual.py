import cv2
import numpy as np
import time
import handTrackingModule as htm
import autopy

######################
wCam, hCam = 640,480
####################


cap = cv2.VideoCapture(0)
cap.set(3,wCam)
cap.set(4,hCam)
pTime = 0
detector =htm.handDetector(maxHands=1)
while True:

    success, img = cap.read()
    img = detector.findHands(img)
    lmList , bbox = detector.findPosition(img)

    if len(lmList)!=0:
        x1,y1 =lmList[8][1:]
        x2,y2 = lmList[12][1:]

        #print(x1,y1,x2,y2)

        fingers = detector.fingersUp()
        print(fingers)


    cTime=time.time()
    fps = 1/(cTime-pTime)
    pTime=cTime
    cv2.putText(img,str(int(fps)),(20,50),cv2.FONT_HERSHEY_PLAIN,3,
                (255,0,0),3)
    cv2.imshow("Image",img)
    cv2.waitKey(1)