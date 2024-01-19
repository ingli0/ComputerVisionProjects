import cv2
import time
import poseModule as pm

cap = cv2.VideoCapture('../videos/1.mp4')
pTime = 0
detector = pm.poseDetector()
while True:
    success, img = cap.read()
    img = detector.findpose(img)
    lmList = detector.getPosition(img)
    print(lmList)
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    if len(lmList) != 0:
        cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
