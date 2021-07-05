import cv2 
import mediapipe as mp 

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

camera = cv2.VideoCapture(1)
print(camera.get(3))
print(camera.get(4))

with mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5, max_num_hands = 1) as hands:
    while camera.isOpened():
        _, image = camera.read()
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False 
        results = hands.process(image)

        image.flags.writeable = True
        #print(results.multi_hand_landmarks)
        if results.multi_hand_landmarks:
            for id, landmark in enumerate(results.multi_hand_landmarks):
                print(f'{id} : {landmark}\n-----\n')
            
        cv2.imshow("Camera No. 1", cv2.cvtColor(image, cv2.COLOR_RGB2BGR))
        if cv2.waitKey(1) & 0xff == ord('q'):
            break 

camera.release()
cv2.destroyAllWindows()