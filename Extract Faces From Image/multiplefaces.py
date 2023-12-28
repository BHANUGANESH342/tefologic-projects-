import cv2
import os

# Set the actual path to the directory containing your images
input_directory = r"C:\Users\rkssp\Desktop\TEFOlogic PROJECTS\Extract Faces From Image\images"
xml_path = r'C:\Users\rkssp\Desktop\TEFOlogic PROJECTS\face blur\haarcascade_frontalface_default.xml'
output_directory = os.path.join(os.getcwd(), 'Extract Faces From Image', 'Faces')

try:
    os.makedirs(output_directory, exist_ok=True)
except FileExistsError as fee:
    print('Exception Occurred:', fee)

faceCascade = cv2.CascadeClassifier(xml_path)

image_files = [f for f in os.listdir(input_directory) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

for image_file in image_files:
    img_path = os.path.join(input_directory, image_file)
    img = cv2.imread(img_path)

    faces = faceCascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=4, minSize=(30, 30))
    i = 1
    scale_factor = 6

    for (x, y, w, h) in faces:
        face_img = img[y:y + h, x:x + w]
        scaled_face = cv2.resize(face_img, (w * scale_factor, h * scale_factor))

        cv2.imshow(f"Face {i} - High Resolution", scaled_face)
        cv2.waitKey(0)

        filename = f'Face_{i}_HighRes_{image_file}'
        cv2.imwrite(os.path.join(output_directory, filename), scaled_face)
        i += 1

cv2.destroyAllWindows()


