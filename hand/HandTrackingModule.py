import cv2
import mediapipe as mp
import numpy as np

import time


class handDetector():
    def __init__(self, mode=False,maxHands=2,detectionCon=0.5,trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon= trackCon
        self.tipIds = [4, 8, 12, 16, 20]
        self.fingers = []
        self.lmList = []


        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(static_image_mode=self.mode,
                                        max_num_hands=self.maxHands,
                                        min_detection_confidence=self.detectionCon,
                                        min_tracking_confidence=self.trackCon)

        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self,img,draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)



        self.results = self.hands.process(imgRGB)

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:

                if draw:
                    self.mpDraw.draw_landmarks(img,handLms,
                                               self.mpHands.HAND_CONNECTIONS)
        return img

    def findPosition(self, img, handNo=0, draw=True):
        xList= []
        yList = []
        bbox =[]
        self.lmList=[]
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                xList.append(cx)
                yList.append(cy)
                self.lmList.append([id,cx,cy])
                if draw:
                    cv2.circle(img, (cx, cy), 5, (255, 0, 255), cv2.FILLED)

            # Calculate bounding box
            xmin ,xmax = min(xList),max(xList)
            ymin,ymax = min(yList),max(yList)

            if draw:
                cv2.rectangle(img,(xmin - 20,ymin-20),(xmax+20,ymax+20),
                              (0,255,0),2)

        return self.lmList, bbox


    def fingersUp(self):
        """
        Finds how many fingers are open and returns in a list.
        Considers left and right hands separately
        :return: List of which fingers are up
        """
        fingers = []

        if self.results.multi_hand_landmarks:
            fingers = []
            # Thumb

            if self.lmList[self.tipIds[0]][1] > self.lmList[self.tipIds[0] - 1][1]:
                    fingers.append(1)
            else:
                    fingers.append(0)


            # 4 Fingers
            for id in range(1, 5):
                if self.lmList[self.tipIds[id]][2] < self.lmList[self.tipIds[id] - 2][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)
        return fingers



def main():
 pTime = 0
 cTime = 0
 cap = cv2.VideoCapture(0)
 detector = handDetector()
 while True:
     succes, img = cap.read()
     img=detector.findHands(img)
     lmList=detector.findPosition(img,draw=False)
     if len(lmList)!=0:
         print(lmList[4])


     #display framerate per second
     cTime = time.time()
     fps = 1/(cTime-pTime)
     pTime = cTime

     cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,3,
                 (255,0,255),3)

     cv2.imshow("image",img)
     cv2.waitKey(1)



if __name__ == "__main__":
 main()