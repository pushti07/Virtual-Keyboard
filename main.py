import cv2
import mediapipe as mp
from pynput.keyboard import Controller
from time import sleep
import math

# Initialize the camera
cap = cv2.VideoCapture(0)

# Initialize MediaPipe Hands
mphands = mp.solutions.hands
Hands = mphands.Hands()
mpdraw = mp.solutions.drawing_utils

# Define the keyboard layout
keys = [["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
        ["A", "S", "D", "F", "G", "H", "J", "K", "L", ";"],
        ["Z", "X", "C", "V", "B", "N", "M", ",", ".", "/"]]

keyboard = Controller()

# Store class to manage button properties
class Store():
    def __init__(self, pos, size, text):
        self.pos = pos
        self.size = size
        self.text = text

# Function to draw the virtual keyboard
def draw(img, storedVar):
    for button in storedVar:
        x, y = button.pos
        w, h = button.size
        cv2.rectangle(img, button.pos, (x + w, y + h), (64, 64, 64), cv2.FILLED)
        cv2.putText(img, button.text, (x + 10, y + 43), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 255), 2)
    return img

# Initialize the stored variable list for the buttons
StoredVar = []
for i in range(len(keys)):
    for j, key in enumerate(keys[i]):
        StoredVar.append(Store([60 * j + 10, 60 * i + 10], [50, 50], key))

# Variable to store the typed word
typed_word = ""

# Main loop to capture frames and process hand landmarks
while cap.isOpened():
    success_, img = cap.read()
    if not success_:
        break

    img = cv2.flip(img, 1)
    cvtImg = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = Hands.process(cvtImg)
    lmlist = []

    if results.multi_hand_landmarks:
        for img_in_frame in results.multi_hand_landmarks:
            mpdraw.draw_landmarks(img, img_in_frame, mphands.HAND_CONNECTIONS)

        for id, lm in enumerate(results.multi_hand_landmarks[0].landmark):
            h, w, c = img.shape
            cx, cy = int(lm.x * w), int(lm.y * h)
            lmlist.append([cx, cy])

    if lmlist:
        for button in StoredVar:
            x, y = button.pos
            w, h = button.size

            if x < lmlist[8][0] < x + w and y < lmlist[8][1] < y + h:
                cv2.rectangle(img, (x - 5, y - 5), (x + w + 5, y + h + 5), (0, 0, 255), cv2.FILLED)
                x1, y1 = lmlist[8][0], lmlist[8][1]
                x2, y2 = lmlist[12][0], lmlist[12][1]
                l = math.hypot(x2 - x1, y2 - y1)
                if l < 50:
                    typed_word += button.text
                    keyboard.press(button.text)
                    keyboard.release(button.text)
                    cv2.rectangle(img, (x - 5, y - 5), (x + w + 5, y + h + 5), (0, 255, 0), cv2.FILLED)
                    sleep(0.3)

    img = draw(img, StoredVar)
    
    # Draw the typed word on the screen
    cv2.putText(img, typed_word, (10, 350), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 3)
    
    cv2.imshow("Hand Tracking", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
