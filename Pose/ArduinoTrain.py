import cv2
import numpy as np
import time
import poseModule as pm
import serial

arduino = serial.Serial('COM3', 9600, timeout=1)  # Change 'COM3' to your port
time.sleep(2)  # Allow some time for Arduino to initialize
cap = cv2.VideoCapture(0)  # Using the default camera (change index if you have multiple cameras)

# Set camera resolution
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

detector = pm.poseDetector()
count = 0
dir = 0
pTime = 0

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)  # Flip the image horizontally for a mirror view

    img = cv2.resize(img, (1280, 720))  # Resize for processing if necessary

    img = detector.findPose(img, False)
    lmList = detector.findPosition(img, False)

    if len(lmList) != 0:
        angle = detector.findAngle(img, 12, 14, 16)
        per = np.interp(angle, (210, 310), (0, 100))
        bar = np.interp(angle, (220, 310), (650, 100))

        color = (255, 0, 255)
        if per == 100:
            color = (0, 255, 0)
            if dir == 0:
                count += 0.5
                dir = 1
        if per == 0:
            color = (0, 255, 0)
            if dir == 1:
                count += 0.5
                dir = 0


        arduino.write(str(count).encode())
        # Draw Curl Count
        cv2.rectangle(img, (0, 450), (250, 720), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, str(int(count)), (45, 670), cv2.FONT_HERSHEY_PLAIN, 15,
                    (255, 0, 0), 25)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (50, 100), cv2.FONT_HERSHEY_PLAIN, 5,
                (255, 0, 0), 5)

    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to quit
        break

cap.release()
cv2.destroyAllWindows()
