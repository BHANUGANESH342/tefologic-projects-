# import the necessary packages
import cv2

# initialize the video capture and face cascade classifier
cap = cv2.VideoCapture(0)
faceCascade = cv2.CascadeClassifier(r"C:\Users\rkssp\Desktop\TEFOlogic PROJECTS\face blur\haarcascade_frontalface_default.xml")
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')


# loop over frames from the video stream
while True:
    # read the current frame
    success, img = cap.read()

    # detect faces in the frame
    faces = faceCascade.detectMultiScale(img, 1.2, 4)

    # loop over the faces
    for (x, y, w, h) in faces:
        # extract the ROI of the face
        ROI = img[y:y + h, x:x + w]

        # blur the ROI
        blur = cv2.GaussianBlur(ROI, (91, 91), 0)

        # insert the blurred ROI back into the image
        img[y:y + h, x:x + w] = blur

        # draw a bounding box around the face
        # cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 4)

    # check to see if any faces were found
    if len(faces) == 0:
        # draw a message if no faces were found
        cv2.putText(img, 'No Face Found!', (20, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255))

    # display the processed frame
    cv2.imshow('Face Blur', img)

    # quit the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('e'):
        break

# release the video capture and close the window
cap.release()
cv2.destroyAllWindows()