import cv2
import mediapipe as mp
import pyautogui
distance_threshold = 100

webcam = cv2.VideoCapture(0)
x1=x2=y1=y2=0
my_hand = mp.solutions.hands.Hands()
drawing_utils=mp.solutions.drawing_utils
while True:
    _,image = webcam.read()
    image=cv2.flip(image,1)
    frame_height,frame_width,_ = image.shape
    rgb_image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    output = my_hand.process(rgb_image)
    hands = output.multi_hand_landmarks
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(image,hand)
            landmarks = hand.landmark
            for id, lm in enumerate(landmarks):
                x=int(lm.x * frame_width)
                y=int(lm.y * frame_height)
                if id == 8:
                    cv2.circle(img=image,center=(x,y),radius=8,color=(255,0,0),thickness=3)
                    x1=x
                    y1=y
                if id == 4:
                    cv2.circle(img=image, center=(x, y), radius=8, color=(255, 0, 0), thickness=3)
                    x2=x
                    y2=y
        dist=((x2-x1)**2+(y2-y1)**2)**0.5//4
        cv2.line(image,(x1, y1), (x2, y2),(0, 255, 0), thickness=5)
        if dist > 30:
            pyautogui.press("volumeUp")
        else:
            pyautogui.press("volumeDown")

    cv2.imshow("hand volume control by the karan ", image)
    key = cv2.waitKey(10)
    if key == 27:
        break
webcam.release()
cv2.destroyAllWindows()


