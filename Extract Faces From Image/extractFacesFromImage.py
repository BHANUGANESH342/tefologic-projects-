import cv2
import os

# Provide the correct paths to your image and XML file
img_path = r"C:\Users\rkssp\Desktop\bharathi.jpg"
xml_path = r'C:\Users\rkssp\Desktop\TEFOlogic PROJECTS\face blur\haarcascade_frontalface_default.xml'

# Read the image
img = cv2.imread(img_path)

# Check if the image is successfully loaded
if img is None:
    raise IOError(f"Error loading image at path: {img_path}")

# Initialize the face cascade
faceCascade = cv2.CascadeClassifier(xml_path)

# Check if the face cascade is successfully loaded
if faceCascade.empty():
    raise IOError(f"Error loading haarcascade_frontalface_default.xml at path: {xml_path}")

# Perform face detection
faces = faceCascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=4, minSize=(30, 30))

# Check if any faces are detected
if len(faces) == 0:
    print("No faces detected.")

# Set the output directory
output_directory = os.path.join(os.getcwd(), 'Extract Faces From Image', 'Faces')

# Create the output directory if it doesn't exist
try:
    os.makedirs(output_directory, exist_ok=True)
except FileExistsError as fee:
    print('Exception Occurred:', fee)

# Change to the output directory
os.chdir(output_directory)

# Set a scale factor for resizing the faces
scale_factor = 6

# Loop through each detected face
for i, (x, y, w, h) in enumerate(faces, start=1):
    # Crop the face region
    face_img = img[y:y + h, x:x + w]

    # Resize the face
    scaled_face = cv2.resize(face_img, (w * scale_factor, h * scale_factor))

    # Display the scaled face (for Jupyter Notebook)
    cv2.imshow(f"Face {i} - High Resolution", scaled_face)
    cv2.waitKey(0)

    # Save the scaled face on disk
    filename = f'Face_{i}_HighRes.jpg'
    cv2.imwrite(filename, scaled_face)

# Close any open OpenCV windows (for Jupyter Notebook)
cv2.destroyAllWindows()
