from __future__ import print_function
from PIL import Image
from picamzero import Camera
import os
import cv2 as cv
import argparse
import numpy as np
import requests


def take_and_crop_photo():

    # Define length and height of each image
    length = 2592 
    height = 1944
    cropped_height = height * (1/3)

    # Define region of interest values
    # These will need further definitions and error checking.

    roi_one_x1 = 0
    roi_one_y1 = 648
    roi_one_x2 = 864
    roi_one_y2 = 1296

    roi_two_x1 = 864
    roi_two_y1 = 648
    roi_two_x2 = 1728
    roi_two_y2 = 1296

    roi_three_x1 = 864
    roi_three_y1 = 1296
    roi_three_x2 = 2592
    roi_three_y2 = 1296
    

    home_dir = os.environ['~']
    cam = Camera()

    cam.start_preview()
    cam.take_photo(f"{home_dir}/img/img.jpg")
    cam.stop_preview()

    img_parent = Image.open(f"{home_dir}/img/img.jpg")
    img_parent = img_parent.crop((0, cropped_height, length, height))

    img_manipulate = cv2.imread(f"{home_dir}/img/img.jpg")

    # Define ROIs for image
    roi_parking_spot_one = img_parent[1296:648, 0:864]
    roi_parking_spot_two = img_parent[1296:648, 1728:]
    roi_parking_spot_three = img_parent[1296:1296, 864:2592]

    cv2.imshow("Show selected ROI: ", roi_parking_spot_one)
    cv2.imshow("Show selected ROI: ", roi_parking_spot_two)
    cv2.imshow("Show selected ROI: ", roi_parking_spot_three)

    


def detect_cars(frame):
    # Car Detection Testing with online image
    
    frame = frame.resize((450, 250))

    # convert image into numpy array
    image_arr = np.array(frame)

    # Convert image to greyscale
    frame_grey = cv.cvtColor(image_arr, cv.COLOR_BGR2GRAY)
    Image.fromarray(frame_grey)

    # Remove noise from the image
    frame_blur = cv.GaussianBlur(frame_grey, (5,5), 0)
    Image.fromarray(frame_blur)

    # Dilate the image
    frame_dilated = cv.dilate(frame_blur, np.ones((3,3)))
    Image.fromarray(frame_dilated)

    kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (2, 2))
    closing = cv.morphologyEx(frame_dilated, cv.MORPH_CLOSE, kernel)

    Image.fromarray(closing)

    # Need car cascade to detect cars

    # Need to define a deadzone on the street
    # - Crop original image to remove the street

    car_cascade_src = 'cars.xml'
    car_cascade = cv.CascadeClassifier(car_cascade_src)
    cars = car_cascade.detectMultiScale(closing, 1.1, 1)

    # Draw rectangles around cars

    count = 0
    for (x, y, w, h) in cars:
        cv.rectangle(image_arr, (x,y), (x+w, y+h), (255, 0, 0), 2)
        count += 1

    print(count, " cars found")
    Image.formarray(image_arr)

    


    
    