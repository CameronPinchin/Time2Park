# Time2Park
 Smart parking availability detector. 

Time2Park is a personal project aimed at utilizing a Raspberry Pi and Pi-Cam 
to analyze the parking spots directly out front of my house. 

This project aims to build upon my knowledge of Python and SQL to improve my proficency as a programmer, in addition to it being an interesting personal project. 

This project will be deployable for anyone who has a Raspberry Pi and Picamera. You just need a location that has visible access to parking parking spots in a similar fashion that I have. 

From my living room window, there are three spots directly infront of my house where you can park. If this differs from your situation, then you will need to adjust the rois defined in car_detection.py accordingly. To learn more about ROIs and how you would adjust them, I will link the openCV documentation below.

https://docs.opencv.org/4.x/index.html


Database Descriptions:

- PARKINGSPOT TABLE
  -          ID: INTEGER, acts as a primary key for obtaining data on a given parking spot
  - parkingSpot: INTEGER, provides us with the parking spot number (1,2,3).
  -  isOccupied: INTEGER, equivalent to a boolean, 0 if empty, 1 if occupied.
  -   TIMESTAMP: Provides us with the time the photo was taken.
- PARKINGSPOT TABLE stores unrefined raw data after image analysis, to then be queried and analyzed. The refined
  data will then be sent to the ANALYSIS Table.

- ANALYSIS TABLE
  -          ID: INTEGER, acts as a primary key for obtaining data on a given parking spot
  - parkingSpot: INTEGER, provides us with the parking spot number (1,2,3).
  - peak_availability_start: TEXT, provides us with the start-time when a space is available for the longest period of time on a given day.
  -   peak_availability_end: TEXT, provides us with the end-time when a space is available for the longest period of time on a given day.
  -    peak_occupancy_start: TEXT, provides us with the start-time when a space is occupied for the longest period of time on a given day.
  -      peak_occupancy_end: TEXT, provides us with the end-time when a space is occupied for the longest period of time on a given day.
  -      avg_occupancy_rate: REAL, provides us with the average amount of time on a given day a space is occupied.
  -   avg_availability_rate: REAL, provides us with the average amount of time on a given day a space is available for parking.

  
