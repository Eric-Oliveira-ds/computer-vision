import cv2
import matplotlib.pyplot as plt
import mediapipe as mp

# capturar video 
cap = cv2.VideoCapture('Pose Estimation Videos/video1-25fps.mp4')

while True:
    success, img = cap.read()
    cv2.imshow("Image", img)
    cv2.waitKey(1)