import cv2
import os

path = os.path.dirname(os.getcwd()) + "/SmokingDartsv2/images/test"
print(path)

# Set up the cameras
camX = cv2.VideoCapture(1) # First camera connected to USB port 0
camY = cv2.VideoCapture(2) # Second camera connected to USB port 1

# Read an image from each camera
ret1, img1 = camX.read()
ret2, img2 = camY.read()

# Check if images were captured successfully
if not ret1:
    print("Unable to capture image from camera 1")
    exit()
if not ret2:
    print("Unable to capture image from camera 2")
    exit()

# Save the images to your desktop
cv2.imwrite(os.path.join(path, "camX.jpeg"), img1)
cv2.imwrite(os.path.join(path, "camY.jpeg"), img2)

# Release the cameras
camX.release()
camY.release()

print("Done")