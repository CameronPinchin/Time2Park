# Cameron Pinchin
# March 6th, 2025
# Planned Purpose: To query the DB, perform calculations and analysis on data present
#                  - Will say when you would be most likely to get a parking spot
#                  - Other considerations: Time when a spot is empty for the longest period
#                  -       

import sqlite3 
import numpy
import cv2
from picamera2 import Picamera2

# Connnect with the DB
imageDB = sqlite3.connect("imageDB.db")
cursor = imageDB.cursor()


