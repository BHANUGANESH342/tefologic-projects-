import cv2
from cvzone.HandTrackingModule import HandDetector

# Open the camera
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

# Initialize Hand Detector
detector = HandDetector(detectionCon=0.7)

while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)

    if len(hands) == 2:
        hand1 = hands[0]
        hand2 = hands[1]

        # Calculate the distance between the hands
        length, _, _ = detector.findDistance(hand1["center"], hand2["center"], img)

        # Adjust the scaling factor based on the distance
        scale = int((length - 50) // 2)  # Adjust the divisor as needed for a smoother zoom

        # Resize the entire image while preserving color
        newH, newW = img.shape[0] + scale, img.shape[1] + scale
        img_resized = cv2.resize(img, (newW, newH))

        # Display the resized image
        cv2.imshow("Zoomed Frame", img_resized)

    # Add a slight delay to allow for smooth processing
    cv2.waitKey(0)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
