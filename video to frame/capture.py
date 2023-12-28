import cv2
import os

def capture_frames_and_save(output_path):
    # Open the default camera (camera index 0)
    cap = cv2.VideoCapture(0)

    # Create the output folder if it doesn't exist
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    frame_number = 0

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Display the resulting frame
        cv2.imshow('Camera Feed', frame)

        # Save the frame
        frame_filename = f"{output_path}/frame_{frame_number}.png"
        cv2.imwrite(frame_filename, frame)

        # Increment frame number
        frame_number += 1

        # Break the loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

# Example usage
output_path = "C:/Users/rkssp/Downloads/video_to_frame_data"
capture_frames_and_save(output_path)
