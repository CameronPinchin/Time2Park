from __future__ import print_function
from PIL import Image
import cv2 as cv
import argparse
import numpy as np
import requests

def detectCars(frame):
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

    


    
    