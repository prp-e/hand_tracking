import cv2 
import mediapipe as mp 

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

camera = cv2.VideoCapture(1)

with mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5) as hands:
    while camera.isOpened():
        _, image = camera.read()

        cv2.imshow("Camera No. 1", image)
        if cv2.waitKey(1) & 0xff == ord('q'):
            break 

camera.release()
cv2.destroyAllWindows()