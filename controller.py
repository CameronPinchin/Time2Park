#   Author: Cameron Pinchin
#     Date: March 23rd, 2025
#  Purpose: Controller / Main function for controlling each script as one, allowing for easy start / stop. 
#            - Planning to add direct keyboard controls. I.e., Press 1 to start, Press 2 to stop, and so on.



import car_detection
import db_init

def main():

    conn, cursor = db_init.db_initialize()
    car_detection.take_and_crop_photo(conn, cursor)

if __name__ == "__main__":
    main()