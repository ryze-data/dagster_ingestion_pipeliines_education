"""
This asset module consists of downloading nces Common Core of Data

This code was adopted from a git repo and modified a bit to function without errors
"""

import os  # used to navigate and perform operations on directories
import subprocess  # used in unzip function

import openpyxl  # used to load and convert excel documents to txt files
import requests  # used to load url zip files

from . import constants  # used to load common variables

from dagster import (
    get_dagster_logger,
    asset,
)  # used to load functions as assets by dagster
import time


@asset(group_name="NCES")
def nces_ccd_files():
    """
    This asset will download zip files, unzip the file, write to the specified directory

    IF you get a requests.exceptions.ChunkedEncodingError: ('Connection broken: IncompleteRead(9145 bytes read, 855 more expected)
    THEN the pipeline
    """
    dagster_logger = get_dagster_logger()
    # Required variables. Variables defined in constants.py"
    input_dir = constants.DOWNLOAD_DIRECTORY
    nces_url_batches = [
        # constants.NCES_URLS_BATCH_1,
        # constants.NCES_URLS_BATCH_2,
        # constants.NCES_URLS_BATCH_3,
        # constants.NCES_URLS_BATCH_4,
        # constants.NCES_URLS_BATCH_5,
        constants.NCES_URLS_BATCH_6,
        # constants.NCES_URLS_BATCH_7,
        # constants.NCES_URLS_BATCH_8,
    ]

    # Required functions
    def unzip(path, target_dir):
        """
        This asset unzips the file

        Args:
            path - the folder path where the file is located
            target_dir - the directory the folder path is located
        """
        # built-in zipfile library chokes on some files
        # import zipfile
        # with zipfile.ZipFile(path, 'r') as zip_ref:
        #     zip_ref.extractall(target_dir)
        # use code below unzip.exe instead (note requires git install)
        subprocess.run(
            ["C:/Program Files/Git/usr/bin/unzip.exe", "-o", path, "-d", target_dir],
            check=True,
        )

    # had to break these apart into batches to avoid connection error from server
    for batch in nces_url_batches:
        dagster_logger.info("#######\nStarting Next Batch\n######")
        dagster_logger.info(batch)
        dagster_logger.info(
            "Step 1: Download zip file, unzip file, clean up all unnecessary files"
        )
        for url in batch:
            base = url[url.rindex("/") + 1 :]
            path = os.path.join(input_dir, base)

            dagster_logger.info(path)

            # download url zip files
            if not os.path.exists(path):
                dagster_logger.info(f"Downloading {url}")
                with requests.get(url, stream=True) as r:
                    r.raise_for_status()
                    with open(path, "wb") as f:
                        # This was added because some csv files were too big and it killed the request
                        for chunk in r.iter_content(chunk_size=10000):
                            # If you have chunk encoded response uncomment if
                            # and set chunk_size parameter to None.
                            # if chunk:
                            f.write(chunk)

                    dagster_logger.info(f"Unzipping {path}")
                    unzip(path, input_dir)

            else:
                dagster_logger.info(f"Skipping {url}")

            # Below code was added to get rid of other files due to storage constraints.
            # Comment below code out if you want to keep all the files.
            # clean up directory
            # for root, dirs, files in os.walk(input_dir):
            #     for file in files:
            #         if not file.endswith(
            #             (".zip", ".txt", ".TXT", ".xlsx", ".csv", ".dat")
            #         ):
            #             os.remove(os.path.join(root, file))

        dagster_logger.info("Batch Complete. Waiting 120 seconds")
        time.sleep(120)

    #### these are zip files within zip files

    if not os.path.exists(os.path.join(input_dir, "ccd_SCH_052_2122_l_1a_071722.csv") and os.path.exists(os.path.join(input_dir, "ccd_SCH_052_2122_l_1a_071722_CSV.zip"))):
        unzip(
            os.path.join(input_dir, "ccd_SCH_052_2122_l_1a_071722_CSV.zip"), input_dir
        )

    if not os.path.exists(os.path.join(input_dir, "ccd_SCH_052_1718_l_1a_083118.csv"))  and os.path.exists(os.path.join(input_dir, "ccd_SCH_052_1718_l_1a_083118 CSV.zip")) :
        unzip(
            os.path.join(input_dir, "ccd_SCH_052_1718_l_1a_083118 CSV.zip"), input_dir
        )



    # Required functions
    def empty_str_to_none(s):
        return None if s == "" else s

    dagster_logger.info(
        "Step 2. each file in the GEOCODECONVERT list will be converted to a text file"
    )
    for file in constants.GEOCODECONVERT:

        geocode = os.path.join(input_dir, file[1])

        if not os.path.exists(geocode):
            dagster_logger.info("Converting geocode file " + file[0] + " to TXT...")

            workbook = openpyxl.load_workbook(
                filename=os.path.join(input_dir, file[0]), read_only=True
            )
            sheet = workbook.active
            rows = sheet.values

            with open(geocode, "w") as output_file:
                for row in rows:
                    output_file.write(
                        "|".join([empty_str_to_none(str(value)) for value in row])
                    )
                    output_file.write("\n")

    # this was added to get rid of other files due to storage constraint issues.
    # Comment below code out if you want to keep all the files.
    # dagster_logger.info("clean up directory")
    # for root, dirs, files in os.walk(input_dir):
    #     for file in files:
    #         if not file.endswith((".txt", ".csv", ".dat", ".TXT")):
    #             os.remove(os.path.join(root, file))
