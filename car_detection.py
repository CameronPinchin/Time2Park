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
    car_cascade_src = 'cars.xml'
    car_cascade = cv.CascadeClassifier(car_cascade_src)
    cars = car_cascade.detectMultiScale(closing, 1.1, 1)

    # Draw rectangles around cars

    count = 0
    for (x, y, w, h) in cars:
        cv.rectangle(image_arr, (x,y), (x+w, y+h), (255, 0, 0), 2)
        count += 1

    print(count, " cars found")
    Image.fromarray(image_arr)


testImage1 = Image.open(requests.get('https://a57.foxnews.com/media.foxbusiness.com/BrightCove/854081161001/201805/2879/931/524/854081161001_5782482890001_5782477388001-vs.jpg',
                                stream=True).raw)

detectCars(testImage1)

    


    
    