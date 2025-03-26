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


def find_day(conn, cur):

    # Gather unique IDs
    entry_ids = cur.execute("SELECT DISTINCT ID FROM PARKINGSPOT")
    unique_ids = []
    for ids in entry_ids:
        id = ids[0]
        unique_ids.append(id)

    # Store unique dates within database
    dates = cur.execute("SELECT DISTINCT DATE(TIMESTAMP) FROM PARKINGSPOT")

    # Begin search based on dates to calculate data for each day
    for date_tuple in dates:
        date = date_tuple[0]
        date_string_start = f"{date} 12:00:00"
        date_string_end = f"{date} 23:30:00"
        search_string = "SELECT * FROM PARKINGSPOT WHERE TIMESTAMP BETWEEN ? AND ?"

        data_for_the_day = cur.execute(search_string, (date_string_start, date_string_end))
        for data in data_for_the_day:
            id, parking_spot, is_occupied, timestamp = data
            print(f"ID: {id}, Spot #: {parking_spot}, Occupied: {is_occupied}, Timestamp: {timestamp}")

           


find_day(imageDB, cursor)

        



