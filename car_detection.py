from __future__ import print_function
from PIL import Image
import cv2 as cv
import argparse
import numpy as numpy
import requests

def detectAndDisplay(frame):
    # Car Detection Testing with online image
    image = Image.open(requests.get('https://a57.foxnews.com/media.foxbusiness.com/BrightCove/854081161001/201805/2879/931/524/854081161001_5782482890001_5782477388001-vs.jpg',
                                    stream=True).raw)
    
    frame = frame.resize((450, 250))

    # convert image into numpy array
    image_arr = np.array(image)

    # Convert image to greyscale
    frame_grey = cv.cvtColor(image_arr, cv.COLOR_BGR2GRAY)
    Image.formarray(frame_grey)

    # Remove noise from the image
    frame_blur = cv.GaussianBlur(frame_grey, (5,5), 0)
    Image.formarray(frame_blur)

    # Dilate the image
    frame_dilated = cv.dilate(frame_blur, np.ones((3,3)))
    Image.formarray(frame_dilated)

    kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (2, 2))
    closing = cv.morphologyEx(dilated, cv.MORPH_CLOSE, kernel)

    Image.formarray(closing)

    # Need car cascade to detect cars

    # Need to define a deadzone on the street
    # It should not detect the presence
    # of cars driving by on the street, as that
    # would skew data heavily.

    car_cascade_src = '../input/carandbusdetection/Required Files/cars.xml'
    car_cascade = cv.CascadeClassifier(car_cascade_src)
    cars = car_cascade.detectMultiScale(closing, 1.1, 1)

    # Draw rectangles around cars

    count = 0
    for (x, y, w, h) in cars:
        cv.rectangle(image_arr, (x,y), (x+w, y+h), (255, 0, 0), 2)
        count += 1

    print(count, " cars found")
    Image.formarray(image_arr)

    


    
    