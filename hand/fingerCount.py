import cv2
import time
import os
import handTrackingModule as htm

wCam,hCam = 1280 ,720

cap = cv2.VideoCapture(0)
cap.set(3,wCam)
cap.set(3,hCam)

folderPath = "fingers"
myList = os.listdir(folderPath)
print(myList)
overlayList = []

for imPath in myList:
    image = cv2.imread(f'{folderPath}/{imPath}')
    overlayList.append(image)

print(len(overlayList))
pTime = 0

detector = htm.handDetector(detectionCon=0.75)

tipIds =[4,8,12,16,20]


while True:

    success, img = cap.read()
    img=detector.findHands(img)
    lmList = detector.findPosition(img,draw=False)
    #print(lmList)


    if len(lmList)!=0:
        fingers= []

        #thumb
        if lmList[tipIds[0]][1] < lmList[tipIds[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)

        #4 fingers
        for id in range(1,5):
            if lmList[tipIds[id]][2] < lmList[tipIds[id]-2][2]:
                fingers.append(1)
            else:
                fingers.append(0)

        #print(fingers)
        totalFingers = fingers.count(1)
        print(totalFingers)

        overlayList_resized = [cv2.resize(overlay, (200, 200)) for overlay in overlayList]
        img[0:200, 0:200] = overlayList_resized[totalFingers-1]


    cTime = time.time()
    fps= 1/(cTime-pTime)
    pTime= cTime

    cv2.putText(img,f'FPS:{int(fps)}',(400,70),cv2.FONT_HERSHEY_PLAIN,
                3,(255,0,0),3)
    cv2.imshow("Image", img)
    cv2.waitKey(1)