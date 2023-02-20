# rotate every image in current directory by 90 degrees
import os
import cv2

# acquire path to images directory
cur_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(cur_dir)
images_dir = os.path.join(parent_dir, 'images')

# get all images in images directory with .jpg extension
images = [f for f in os.listdir(images_dir) if f.endswith('.jpg')]
print("found images:", images)

# rotate every image by 90 degrees
for image in images:
    print(os.path.join(images_dir, image))
    img = cv2.imread(os.path.join(images_dir, image))
    img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
    cv2.imwrite(os.path.join(images_dir, image), img)
