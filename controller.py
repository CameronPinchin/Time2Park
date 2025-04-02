#   Author: Cameron Pinchin
#     Date: March 23rd, 2025
#  Purpose: Controller / Main function for controlling each script as one, allowing for easy start / stop. 
#            - Added exit handler to ensure files are deleted on shutdown.
import car_detection
import db_init
import sys

def main():
    try:
        conn, cursor = db_init.db_initialize()
        car_detection.take_and_crop_photo(conn, cursor)
    except KeyboardInterrupt:
        print("Shutting down program...")
        car_detection.delete_files()
    sys.exit(0)

if __name__ == "__main__":
    main()