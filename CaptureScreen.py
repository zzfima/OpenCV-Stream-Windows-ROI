import cv2
import imutils
import numpy as np
import pyautogui

capture = cv2.VideoCapture(0)
c = 0
is_move_down = True

while True:
    # Take screenshot
    image = pyautogui.screenshot()
    # convert an image from one color space to another
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    # resize big screenshot to smaller one, save aspect ratio
    image = imutils.resize(image, width=800)

    # get measurements of image
    height, width, n = image.shape
    half_height = int(height / 2)
    half_width = int(width / 2)

    # prepare 4 ROI images
    cropped_frame_1 = image[0: half_height, 0: half_width]
    cropped_frame_2 = image[0: half_height, half_width: width]
    cropped_frame_3 = image[half_height: height, 0: half_width]
    cropped_frame_4 = image[half_height: height, half_width: width]

    # Show images
    cv2.imshow('1', cropped_frame_1)
    cv2.imshow('2', cropped_frame_2)
    cv2.imshow('3', cropped_frame_3)
    cv2.imshow('4', cropped_frame_4)
    key = cv2.waitKey(100)
