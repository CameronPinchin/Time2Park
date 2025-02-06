# Project: Time2Park 
#  Author: Cameron Pinchin
# Purpose: File handles database operations.

import sqlite3

# Create a connection to the database, and initalize the cursor
imageDB = sqlite3.connect("imageDB.db")
cursor = imageDB.cursor()

# Insert test data.
cursor.execute("INSERT INTO PARKINGSPOT (isOccupied) VALUES (1);")

# Commit any changes.
imageDB.commit()

# Select test data.
cursor.execute("SELECT * FROM PARKINGSPOT;")

# Retrieve rows from PARKINGSPOT table
rows = cursor.fetchall()

# Print each row individually.
for row in rows:
    print(row)

# Close connection to SQlite.
imageDB.close()
