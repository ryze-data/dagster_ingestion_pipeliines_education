"""
This asset module consists of downloading s275 Common Core of Data

This code was adopted from a git repo and modified a bit to function without errors
"""

import os  # used to navigate and perform operations on directories
import subprocess  # used in unzip function

import pyodbc
import requests  # used to load url zip files
from . import constants  # used to load common variables
from dagster import (
    get_dagster_logger,
    asset,
)  # used to load functions as assets by dagster
import time
import pandas as pd


@asset(group_name="S275")
def s275_accessdb_files():
    """
    This asset will download zip files, unzip the file, write to the specified directory

    IF you get a requests.exceptions.ChunkedEncodingError: ('Connection broken: IncompleteRead(9145 bytes read, 855 more expected)
    THEN run the pipeline again and you should be fine. This happens because the website's server periodically breaks the connections
    """
    dagster_logger = get_dagster_logger()
    # Required variables. Variables defined in constants.py"
    input_dir = constants.DOWNLOAD_DIRECTORY
    s275_url_batches = [
        constants.S275_URLS_BATCH_1,
        constants.S275_URLS_BATCH_2,
        constants.S275_URLS_BATCH_3,
        constants.S275_URLS_BATCH_4,
        constants.S275_URLS_BATCH_5,
        constants.S275_URLS_BATCH_6,
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
    for batch in s275_url_batches:
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
                while True:
                    try:
                        response = requests.get(url)
                        response.raise_for_status()  # Check for any request errors
                        # Process the response data
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
                        break  # If successful, exit the loop
                    except requests.exceptions.ChunkedEncodingError as e:
                        print(
                            f"Encountered ChunkedEncodingError: {e}. Retrying in {constants.BATCH_WAIT_TIME_SECONDS} seconds..."
                        )
                        time.sleep(
                            constants.BATCH_WAIT_TIME_SECONDS
                        )  # Wait for n seconds before retrying
                    except requests.exceptions.RequestException as e:
                        print(f"Encountered a request exception: {e}")
                        break  # Exit the loop on other request exceptions

            else:
                dagster_logger.info(f"Skipping {url}")
        # the amount of time the pipeline will wait until starting new batch. This solves server timeout errors
        # i.e. Server Connection Broke Error
        time.sleep(constants.BATCH_WAIT_TIME_SECONDS)
        dagster_logger.info(
            f"Batch Complete. Waiting {constants.BATCH_WAIT_TIME_SECONDS} seconds"
        )


@asset(deps=[s275_accessdb_files], group_name="S275")
def s275_csv_files():
    """
    This asset takes the .accdb files and converts them to csv files
    """
    input_dir = constants.DOWNLOAD_DIRECTORY
    dagster_logger = get_dagster_logger()
    # clean up directory
    for root, dirs, files in os.walk(input_dir):
        for file in files:
            if file.endswith(("accdb")):
                # Open access database
                with pyodbc.connect(
                    r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ="
                    + input_dir
                    + "/"
                    + file
                    + ";"
                ) as conn:
                    # Create a cursor object
                    with conn.cursor() as cursor:
                        # Execute a query to retrieve the list of tables in the database
                        for table_entry in cursor.tables(tableType="TABLE"):
                            table_name = table_entry[2]

                            dagster_logger.info("Found table: %s" % (table_name))
                            # get table
                            cursor.execute(f"SELECT * FROM [{table_name}]")
                            rows = cursor.fetchall()

                            column_headers = [
                                column[0].upper() for column in cursor.description
                            ]

                            df = pd.DataFrame.from_records(rows, columns=column_headers)
                            print(
                                f"Writing rows to file...{input_dir}/{table_name.upper()}.csv"
                            )
                            # Writ to csv  file
                            df.to_csv(
                                f"{input_dir}/{table_name.upper()}.csv", index=False
                            )
                            dagster_logger.info(df.head())
