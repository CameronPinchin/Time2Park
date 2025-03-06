# Cameron Pinchin
# March 6th, 2025
# Intended to analyze for the presence of a car using OpenCV


import sqlite3 
import numpy
import cv2
from picamera2 import Picamera2

# Connnect with the DB
imageDB = sqlite3.connect("imageDB.db")
cursor = imageDB.cursor()


