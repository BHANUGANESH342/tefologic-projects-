import cv2
import os
import numpy as np
import mediapipe as mp
import pyautogui
from IPython.display import Image

cap = cv2.VideoCapture(0)  # 0 corresponds to the default camera
hand_detector = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils
screen_width, screen_height = pyautogui.size()
index_y = 0

# Smoothing for mouse movement
smoothening = 12
plocx, plocy = 0, 0
clocx, clocy = 0, 0

while True:
    _, frame = cap.read()  # read data from cap
    frame = cv2.flip(frame, 1)  # Flip the frame
    frame_height, frame_width, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert to RGB
    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks  # Hand landmarks

    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame, hand)  # Draw landmarks on the frame
            landmarks = hand.landmark

            for id, landmark in enumerate(landmarks):
                x = int(landmark.x * frame_width)
                y = int(landmark.y * frame_height)

                # Index finger tip point number is 8
                if id == 8:
                    cv2.circle(img=frame, center=(x, y), radius=30, color=(0, 255, 255))
                    index_x = (screen_width / frame_width) * x
                    index_y = (screen_height / frame_height) * y
                    clocx = plocx + (index_x - plocx) / smoothening
                    clocy = plocy + (index_y - plocy) / smoothening
                    pyautogui.moveTo(clocx, clocy)
                    plocx, plocy = clocx, clocy

                # Thumb tip point number is 4
                if id == 4:
                    cv2.circle(img=frame, center=(x, y), radius=30, color=(0, 255, 255))
                    thumb_x = (screen_width / frame_width) * x
                    thumb_y = (screen_height / frame_height) * y
                    distance = abs(index_y - thumb_y)

                    # Adjust the distance threshold based on your needs
                    if distance < 30:
                        print('select')
                        # Add your selection action here
                        # For example, you might want to click or perform some other action
                        pyautogui.click()
                        pyautogui.sleep(1)

    cv2.imshow('Virtual Mouse', frame)  # Show the frame
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Wait for the 'q' key to exit
        break

# Release the video capture object
cap.release()
# Close all OpenCV windows
cv2.destroyAllWindows()
