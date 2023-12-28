import cv2
import numpy as np

def color_detection(frame, lower, upper, color_name):
    # Convert the frame from BGR to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Create a mask to extract the specified color
    mask = cv2.inRange(hsv, lower, upper)

    # Bitwise-AND the original image and the mask
    result = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow(f'Color Detection ({color_name})', result)

# Open the camera
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        print("Failed to capture frame")
        break

    # Define color ranges for detection (you can add more colors)
    colors = {
        'Blue': ([100, 100, 100], [130, 255, 255]),
        'Green': ([40, 40, 40], [80, 255, 255]),
        'Red': ([0, 100, 100], [10, 255, 255]),  # You may need to wrap around due to red hue
    }

    # Perform color detection for each color range
    for color_name, (lower, upper) in colors.items():
        color_detection(frame, np.array(lower), np.array(upper), color_name)

    cv2.imshow('Original', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
