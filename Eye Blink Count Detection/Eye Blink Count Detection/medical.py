import cv2
import dlib
import numpy as np

# Initialize face detector
detector = dlib.get_frontal_face_detector()

# Initialize video capture (0 for default camera)
cap = cv2.VideoCapture(0)

# Buffer for storing past heart rate estimations
heart_rate_buffer = []

# Function to extract region of interest (ROI) around the detected face
def extract_roi(frame, face):
    x, y, w, h = face.left(), face.top(), face.width(), face.height()
    roi = frame[y:y + h, x:x + w]
    return roi

# Function to estimate heart rate from ROI
def estimate_heart_rate(roi):
    # Implement your heart rate estimation algorithm here
    # For simplicity, let's assume a placeholder heart rate
    heart_rate = np.random.randint(60, 100)
    return heart_rate

# Function to apply a simple moving average filter to stabilize heart rate
def stabilize_heart_rate(heart_rate):
    heart_rate_buffer.append(heart_rate)
    buffer_size = 10  # Adjust the buffer size as needed

    if len(heart_rate_buffer) > buffer_size:
        heart_rate_buffer.pop(0)

    stabilized_heart_rate = np.mean(heart_rate_buffer)
    return stabilized_heart_rate

while True:
    # Read a frame from the video capture
    ret, frame = cap.read()

    # Detect faces in the frame
    faces = detector(frame)

    # Process each detected face
    for face in faces:
        # Extract ROI around the face
        roi = extract_roi(frame, face)

        # Estimate heart rate from the ROI
        heart_rate = estimate_heart_rate(roi)

        # Stabilize the heart rate using a moving average filter
        stabilized_heart_rate = stabilize_heart_rate(heart_rate)

        # Display the stabilized heart rate on the frame
        cv2.putText(frame, f"Heart Rate: {stabilized_heart_rate:.2f}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Display the processed frame
    cv2.imshow("Remote Patient Monitoring", frame)

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release video capture and close all windows
cap.release()
cv2.destroyAllWindows()
