import cv2
import time
import mediapipe as mp


class FaceMeshDetector():

    def __init__(self, staticMode=False, maxFaces=2, minDetectionCon=0.5, minTrackCon=0.5):
        self.staticMode = staticMode
        self.maxFaces = maxFaces
        self.minDetectionCon = minDetectionCon
        self.minTrackCon = minTrackCon

        self.mpDraw = mp.solutions.drawing_utils
        self.mpFaceMesh = mp.solutions.face_mesh
        self.faceMesh = self.mpFaceMesh.FaceMesh(
            static_image_mode=False,
            max_num_faces=1,
            min_detection_confidence=0.1,
            min_tracking_confidence=0.1
        )
        self.drawSpec = self.mpDraw.DrawingSpec(thickness=1, circle_radius=1)

    def findFaceMesh(self, img, draw=True):

        self.imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.faceMesh.process(self.imgRGB)
        faces = []

        if self.results.multi_face_landmarks:
            for faceLms in self.results.multi_face_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, faceLms, self.mpFaceMesh.FACEMESH_CONTOURS,
                                               self.drawSpec, self.drawSpec)

                face = []
                for id, lm in enumerate(faceLms.landmark):
                    #print(lm)
                    ih, iw, ic = img.shape
                    x, y = int(lm.x * iw), int(lm.y * ih)
                    cv2.putText(img, str(id), (x, y), cv2.FONT_HERSHEY_PLAIN,
                                0.45, (0, 255, 0),1)
                    #print(id, x, y)
                    face.append([x, y])
                    faces.append(face)

        return img, faces


def main():
    cap = cv2.VideoCapture("../videos/2.mp4")
    pTime = 0
    detection = FaceMeshDetector()

    while True:
        success, img = cap.read()
        img, faces = detection.findFaceMesh(img)

        if len(faces) != 0:
            print(faces[0])

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(img, f'FPS {int(fps)}', (20, 70), cv2.FONT_HERSHEY_PLAIN,
                    3, (0, 255, 0))
        cv2.imshow("Image", img)
        cv2.waitKey(18)


if __name__ == "__main__":
    main()
