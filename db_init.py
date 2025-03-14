# Project: Time2Park 
#  Author: Cameron Pinchin
# Purpose: File defines the database schema, and initalizes the database.


import sqlite3


# Create a connection to the database, and initalize the cursor
imageDB = sqlite3.connect("imageDB.db")
cursor = imageDB.cursor()

cursor.execute("DROP TABLE IF EXISTS PARKINGSPOT")

# Define the table, add attribute for spot 1 - 3
table = """ CREATE TABLE PARKINGSPOT(
            ID INTEGER PRIMARY KEY,
            parkingSpot INTEGER,
            isOccupied INTEGER,
            TIMESTAMP TEXT NOT NULL DEFAULT (CURRENT_TIMESTAMP)
        ); """

# Initialize the table.
cursor.execute(table)

# Close conneciton to SQlite.
cursor.close()