import os
import car_detection
import db_init

def main():

    conn, cursor = db_init.db_initialize()
    car_detection.take_and_crop_photo(conn, cursor)

if __name__ == "__main__":
    main()