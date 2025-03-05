# Project: Time2Park 
#  Author: Cameron Pinchin
# Purpose: File defines the database schema, and initalizes the database.


import sqlite3
from picamera2 import Picamera2

# Create a connection to the database, and initalize the cursor
imageDB = sqlite3.connect("imageDB.db")
cursor = imageDB.cursor()

cursor.execute("DROP TABLE IF EXISTS PARKINGSPOT")

# Define the table
table = """ CREATE TABLE PARKINGSPOT(
            ID INTEGER PRIMARY KEY,
            isOccupied INTEGER,
            TIMESTAMP TEXT NOT NULL DEFAULT (CURRENT_TIMESTAMP)
        ); """

# Initialize the table.
cursor.execute(table)

# Close conneciton to SQlite.
cursor.close()