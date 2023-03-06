# Python program to capture a single image
# using pygame library
  
# importing the pygame library
import pygame
import pygame.camera
import os

print(os.getcwd())

# initializing  the camera
pygame.camera.init()
  
# make the list of all available cameras
camlist = pygame.camera.list_cameras()
print(camlist)
  
# if camera is detected or not
if camlist:
    # initializing the cam variable with default camera
    cam = pygame.camera.Camera(camlist[1], (640, 480))
  
    # opening the camera
    cam.start()
  
    # capturing the single image
    image = cam.get_image()
  
    # saving the image
    pygame.image.save(image, "filename.jpg")
  
# if camera is not detected the moving to else part
else:
    print("No camera on current device")