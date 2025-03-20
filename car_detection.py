#          Author: Cameron Pinchin
#      Start Date: March 6th, 2025
#     Recent Date: March 9th, 2025
#     Description: Program dedicated to analyzing photos
#                  taken from the Pi-Camera to determine
#                  the presence of cars in the three available
#                  spots out front of my house.
# External Sources: cars.xml for detection of cars.
#             link: https://gist.github.com/199995/37e1e0af2bf8965e8058a9dfa3285bc6

from PIL import Image
from picamzero import Camera
import os
import cv2 as cv
import argparse
import numpy as np
import requests

# Define length and height of each image globally
length = 2592 
height = 1944
cropped_height = height * (1/3)


def take_and_crop_photo():
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


def detect_cars(frame):
    
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
    car_cascade_src = 'cars.xml'
    car_cascade = cv.CascadeClassifier(car_cascade_src)
    cars = car_cascade.detectMultiScale(closing, 1.1, 1)

    # Define ROIs for image
    roi_parking_spot_one = cars[648:1296, 0:864]
    roi_parking_spot_two = cars[648:1296, 864:1728]
    roi_parking_spot_three = cars[648:1296, 864:2592]

    # Confirm ROIs were selected properly
    cv.imshow("Show selected ROI: ", roi_parking_spot_one)
    cv.imshow("Show selected ROI: ", roi_parking_spot_two)
    cv.imshow("Show selected ROI: ", roi_parking_spot_three)

    count_roi_one = 0
    count_roi_two = 0
    count_roi_three = 0
    for (y1, y2, x1, x2) in roi_parking_spot_one:
        cv.rectangle(image_arr, (x1+y1),(x1 + x2, y1 + y2), (255, 0, 0), 2)
        count_roi_one += 1

    for (y1, y2, x1, x2) in roi_parking_spot_one:
        cv.rectangle(image_arr, (x1+y1),(x1 + x2, y1 + y2), (255, 0, 0), 2)
        count_roi_two += 1

    for (y1, y2, x1, x2) in roi_parking_spot_one:
        cv.rectangle(image_arr, (x1+y1),(x1 + x2, y1 + y2), (255, 0, 0), 2)
        count_roi_three += 1
    
    # for (x, y, w, h) in cars:
    #    cv.rectangle(image_arr, (x,y), (x+w, y+h), (255, 0, 0), 2)
    #    count += 1

    print(count_roi_one, " cars found in ROI one")
    print(count_roi_two, " cars found in ROI two")
    print(count_roi_three, " cars found in ROI three")
    Image.fromarray(image_arr)


testImage1 = Image.open(requests.get('https://a57.foxnews.com/media.foxbusiness.com/BrightCove/854081161001/201805/2879/931/524/854081161001_5782482890001_5782477388001-vs.jpg',
                                stream=True).raw)

detect_cars(testImage1)

    


    
    