# Project: Time2Park 
#  Author: Cameron Pinchin
# Purpose: File defines the database schema, and initalizes the database.
#          Provides a db_reset() function to reset the db.
import sqlite3
# Create a connection to the database, and initalize the cursor
def db_initialize():
    imageDB = sqlite3.connect("imageDB.db")
    cursor = imageDB.cursor()
    # Define the table, add attribute for spot 1 - 3
    table = """ CREATE TABLE IF NOT EXISTS PARKINGSPOT(
                ID INTEGER PRIMARY KEY,
                parkingSpot INTEGER,
                isOccupied INTEGER,
                TIMESTAMP TEXT NOT NULL DEFAULT (CURRENT_TIMESTAMP)
            ); """
    # Initialize the table.
    cursor.execute(table)
    # Commit changes to DB
    imageDB.commit()
    # Close conneciton to SQlite.
    return imageDB, cursor

def db_reset():
    imageDB = sqlite3.connect("imageDB.db")
    cursor = imageDB.cursor()

    cursor.execute("DROP TABLE IF EXISTS PARKINGSPOT")

    imageDB.commit()

    imageDB.close()