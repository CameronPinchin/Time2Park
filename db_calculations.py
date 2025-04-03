# Cameron Pinchin
# March 6th, 2025
# Planned Purpose: To query the DB, perform calculations and analysis on data present
#                  - Will say when you would be most likely to get a parking spot
#                  - Other considerations: Time when a spot is empty for the longest period
#                  -       

import sqlite3 
import numpy
import cv2
import datetime
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

    timestamps = []
    is_occupied_values = []


    # Begin search based on dates to calculate data for each day
    for date_tuple in dates:
        date = date_tuple[0]
        date_string_start = f"{date} 12:00:00"
        date_string_end = f"{date} 23:59:00"
        date_search_string = "SELECT * FROM PARKINGSPOT WHERE TIMESTAMP BETWEEN ? AND ?"

        cur.execute(date_search_string, (date_string_start, date_string_end))
        data_for_the_day = cur.fetchall()

        for data in data_for_the_day:
            id, parking_one, parking_two, parking_three, timestamp, is_occupied = data
            timestamps.append(datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S"))
            is_occupied_values.append(is_occupied)

# This will need some reworking

            if parking_one == 1:
                parking_spots.append(0)
            elif parking_two == 1:
                parking_spots.append(1)
            elif parking_three == 1:
                parking_spots.append(2)


        occupation_streak = []
        parking_spots = []
        start_index = -1

        for i in range(len(is_occupied_values)):
            if is_occupied_values[i] == 0:
                if start_index == -1:
                    start_index = i
            else:
                if start_index == -1:
                    occupation_streak.append((timestamps[start_index], timestamps[i - 1]))
                    start_index = -1

        if start_index != -1:
            occupation_streak.append((parking_spots[start_index], timestamps[start_index], timestamps[-1]))

        streak_duration = [(spot, start, end, (end - start).total_seconds()) for spot, start, end, in occupation_streak]

        for spot, start, end, duration in streak_duration:
            cursor.execute(
                """INSERT INTO ANALYSIS (parkingSpot, peak_availability_start,
                           peak_availability_end, availability_duration) VALUES ?, ?, ?, ?"""
                           (spot, start, end, duration)
                           )
            
            print("Successful insertion into analysis database.")
                   
find_day(imageDB, cursor)

        



