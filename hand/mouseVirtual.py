import cv2
import numpy as np
import handTrackingModule as htm
import time
import autopy

cap = cv2.VideoCapture(0)
cap.set(3,640)