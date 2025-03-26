#          Author: Cameron Pinchin
#      Start Date: March 6th, 2025
#     Recent Date: March 21st, 2025
#     Description: Program dedicated to analyzing photos
#                  taken from the Pi-Camera to determine
#                  the presence of cars in the three available
#                  spots out front of my house.
# External Sources: cars.xml for detection of cars.
#             link: https://gist.github.com/199995/37e1e0af2bf8965e8058a9dfa3285bc6

from PIL import Image
from picamera2 import Picamera2
import os
import cv2 as cv
import argparse
import numpy as np
import requests
import time
import random
import glob2 as glob
import sqlite3

# Define length and height of each image globally
length = 2592 
height = 1944
cropped_height = 648

img_folder = os.path.expanduser("~/Desktop/Time2Park/img/")

#imageDB = sqlite3.connect("imageDB.db")
#cursor = imageDB.cursor()

def take_and_crop_photo(conn, cursor):
# Loop for continuous photo capture, analysis, and insertion into imageDB
# Handles the deletion of photos after analysis, saving space and more secure
    while True:
        # Measures current time with time() import
        # - Produces a random time between current and current + 300 seconds (five minutes)
        # To ensure I am not taking a photo at the same time each day.
        current_time = time.time()
        five_minutes_ahead = current_time + 300

        current_time = current_time // 1
        five_minutes_ahead = five_minutes_ahead // 1
        
        rand_time = random.randint(current_time, five_minutes_ahead)
                
        while True:
        
            # Measure current time again, 
            current_time = time.time()
            if abs(current_time - rand_time):
                print(f"Random time {rand_time} reached, capturing image.")

                img_path = f"{img_folder}{rand_time}.jpg"
                
                cam = Picamera2()
                camera_config = cam.create_preview_configuration(main={"size": (length, height)})
                cam.configure(camera_config)

                cam.start()
                time.sleep(2)
                cam.capture_file(img_path)
                cam.stop()
                cam.close()

                img_parent = cv.imread(img_path)
                                
                detect_cars(img_parent, conn, cursor)

                break
            else:
                time.sleep(0.1) 

        

def detect_cars(frame, conn, cursor):
    # convert image into numpyarray
    image_arr = np.array(frame)
   
    rois = [
        (0, 648, 864, 1296),
        (864, 648, 864, 1296),
        (1728, 648, 864, 1296)
    ]

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
    
    car_counts = {}
    for (x, y, w, h) in rois:
        roi_frame = closing[y:y+h, x:x+w]
        cars = car_cascade.detectMultiScale(roi_frame, scaleFactor=1.2, minNeighbors=10, minSize=(50,50))
        car_counts[(x, y, w, h)] = len(cars)

        for (cx, cy, cw, ch) in cars:
            abs_x = cx + x
            abs_y = cy + y
            cv.rectangle(image_arr, (abs_x, abs_y), (abs_x + cw, abs_y + ch), (0, 255, 0), 2)
            
    for roi, count in car_counts.items():
        print(f"ROI {roi} detected {count} cars")

    add_to_database(car_counts, conn, cursor)

    jpg_files = glob.glob(f"{img_folder}*.jpg")

    for f in jpg_files:
        os.remove(f)
        print(f"Deleted: {f}")

    take_and_crop_photo(conn, cursor)

def add_to_database(counts, conn, cursor):
    just_counts = list(counts.values())

    
    if just_counts[0] == 0:
        cursor.execute('''INSERT INTO PARKINGSPOT (parkingSpot, isOccupied) VALUES (1, 0)''')
    else: 
        cursor.execute('''INSERT INTO PARKINGSPOT (parkingSpot, isOccupied) VALUES (1, 1)''')
    if just_counts[1] == 0:
        cursor.execute('''INSERT INTO PARKINGSPOT (parkingSpot, isOccupied) VALUES (2, 0)''')
    else:
        cursor.execute('''INSERT INTO PARKINGSPOT (parkingSpot, isOccupied) VALUES (2, 1)''')
    if just_counts[2] == 0:
        cursor.execute('''INSERT INTO PARKINGSPOT (parkingSpot, isOccupied) VALUES (3, 0)''')
    else:
        cursor.execute('''INSERT INTO PARKINGSPOT (parkingSpot, isOccupied) VALUES (3, 1) ''')

    conn.commit()

    









    


    
    