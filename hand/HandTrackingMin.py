import cv2
import mediapipe as mp
import time


wCam,hCam = 1280 ,720

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
pTime=0


mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils


cTime = 0

while True:
    succes, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                h,w,c = img.shape
                cx,cy = int(lm.x*w),int(lm.y*h)
                print(id,cx,cy)
                cv2.circle(img,(cx,cy),5,(255,0,255),cv2.FILLED)



            mpDraw.draw_landmarks(img,handLms,mpHands.HAND_CONNECTIONS)

    #display framerate per second
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,3,
                (255,0,255),3)

    cv2.imshow("image",img)
    cv2.waitKey(1)
