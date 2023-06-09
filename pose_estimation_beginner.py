import cv2
import matplotlib.pyplot as plt
import mediapipe as mp
import time

# capturar video 
cap = cv2.VideoCapture('Pose Estimation Videos/video2-25fps.mp4')
pTime = 0
while True:
    # ler video
    success, img = cap.read()

    # checar frame rate
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (90,70), cv2.FONT_HERSHEY_PLAIN, 8, (255, 0, 0), 8)
    cv2.imshow("Image", img)

    key = cv2.waitKey(1)

    # Verifica se a tecla 'q' foi pressionada
    if key == ord('q'):
        break

    # Fecha a janela
cv2.destroyAllWindows()
