# Project: Time2Park 
#  Author: Cameron Pinchin
# Purpose: File handles database operations.

import sqlite3
from picamera2 import Picamera2

# Create a connection to the database, and initalize the cursor
imageDB = sqlite3.connect("imageDB.db")
cursor = imageDB.cursor()

# Every 3-5 minutes take a photo, upload data to the DB.
# Not required to store the whole photo, analyze for the presence of a car
# then store that information in the DB. 

# Commit any changes.
# imageDB.commit()

# Select test data.
# cursor.execute("SELECT * FROM PARKINGSPOT;")

# Retrieve rows from PARKINGSPOT table
rows = cursor.fetchall()

# Print each row individually.
for row in rows:
    print(row)

# Close connection to SQlite.
imageDB.close()
