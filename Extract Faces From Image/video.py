import cv2
import os

video_path = r"C:\Users\rkssp\Desktop\multi faces.mp4"
output_folder = r"C:\Users\rkssp\Desktop\output_faces"

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

vid = cv2.VideoCapture(video_path)

# Load the pre-trained Haar Cascade classifier for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

i = 0
while True:
    grabbed, frame = vid.read()

    if not grabbed:
        break

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.3, minNeighbors=5)

    for (x, y, w, h) in faces:
        face_roi = frame[y:y+h, x:x+w]
        face_filename = os.path.join(output_folder, f"face_{i}.jpg")
        cv2.imwrite(face_filename, face_roi)
        i += 1

        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    cv2.imshow('Frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()
