import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture("../videos/2.mp4")
pTime = 0

mpFaceDetection = mp.solutions.face_detection
mpDraw = mp.solutions.drawing_utils
faceDetection = mpFaceDetection.FaceDetection()


while True:
    success, img = cap.read()

    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results = faceDetection.process(imgRGB)
    print(results)

    if results.detections:
        for id, detection in enumerate(results.detections):
            bboxc = detection.location_data.relative_bounding_box
            ih, iw, ic = img.shape
            bbox = int(bboxc.xmin * iw), int(bboxc.ymin * ih), \
                   int(bboxc.width * iw), int(bboxc.height * ih)
            cv2.rectangle(img, bbox, (255, 0, 255), 2)
            cv2.putText(img, f'{int(detection.score[0] * 100)}% alkolikos ',
                        (bbox[0], bbox[1] - 20), cv2.FONT_HERSHEY_PLAIN,
                        2, (255, 0, 255), 2)

    cv2.imshow("Image",img)
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime=cTime
    cv2.putText(img, f'FPS:{int(fps)}',(20,70),cv2.FONT_HERSHEY_PLAIN,
                    3,(0,255,0),2)
    cv2.imshow("Image",img)
    cv2.waitKey(18)

def main():
    cap = cv2.VideoCapture("../videos/2.mp4")
    pTime = 0


if __name__ == "__main__":
    main()