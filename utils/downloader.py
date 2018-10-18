import requests
import os.path
import sys


def download_as_file(file_name):
    """Download file from https://github.com/planetsig/ufo-reports/raw/master/csv-data/ufo-scrubbed-geocoded-time-standardized.csv 
    and save to file_name from parameters, if already exists, do nothing.."""

    if not os.path.isfile(file_name):

        try:
            print("Downloading file...")
            response = requests.get('https://github.com/planetsig/ufo-reports/raw/master/csv-data/ufo-scrubbed-geocoded-time-standardized.csv')
            as_string = response.text

            with open(file_name, 'w', encoding='utf8', newline='') as the_file:
                the_file.write(as_string)
        except Exception as e:
            print("Error downloading file; ", e)
            sys.exit(1)
        print("File downloaded.")
