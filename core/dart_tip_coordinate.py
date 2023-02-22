# script for getting the dart tip pixel x-coordinate from a dartboard image

# load libraries 
from scipy.ndimage import center_of_mass
from helper_functions import isolate_dart_tip
from dartboard_images import DartboardImage
import cv2
import numpy as np
import matplotlib.pyplot as plt

def get_dart_tip_coordinates(dart, last_img):
    # dartboard
    db = DartboardImage("x", dart, last_img=last_img)
    diff = db.get_diff_to_last_img()

    # set bottom 3/4 of image to 0
    diff[diff.shape[0]//4:, :] = 0

    # opencv dilation
    kernel = np.ones((5,5),np.uint8)
    diff = cv2.dilate(diff.astype('uint8'),kernel,iterations = 1)

    # opencv erosion
    kernel = np.ones((5,5),np.uint8)
    diff = cv2.erode(diff.astype('uint8'),kernel,iterations = 1)

    # get the tip
    isolated_dart_tip = isolate_dart_tip(diff)
    y_coordinate, x_coordinate = center_of_mass(isolated_dart_tip)

    return x_coordinate