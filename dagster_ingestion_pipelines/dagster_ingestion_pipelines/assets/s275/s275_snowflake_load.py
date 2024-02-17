"""
This asset module consists of loading s275 Common Core of Data to Snowflake

This code was adopted from a git repo and modified a bit to function without errors
"""

import os  # used to navigate and perform operations on directories

import pandas as pd

from . import constants, s275_file_download  # used to load common variables

from dagster import (
    get_dagster_logger,
    asset,
)  # used to load functions as assets by dagster
from dagster_snowflake import SnowflakeResource
from snowflake.connector.pandas_tools import write_pandas


@asset(deps=[s275_file_download.s275_csv_files], group_name="S275")
def snowflake_s275_raw_tables(snowflake: SnowflakeResource):
    dagster_logger = get_dagster_logger()
    # get directory
    input_dir = constants.DOWNLOAD_DIRECTORY
    # for each file in directory
    for root, dirs, files in os.walk(input_dir):
        for file in files:
            if file.endswith((".csv")):
                dagster_logger.info(file)
                table_name = os.path.basename(file).split('.')[0]

                dagster_logger.info(f"printing file: {table_name}")
                path = os.path.join(root, file)
                df = pd.read_csv(f"{path}", dtype=str, encoding="utf-8").astype(str)
                with snowflake.get_connection() as conn:
                    write_pandas(
                        conn,
                        df,
                        table_name.upper(),
                        auto_create_table=True,
                        overwrite=True,
                    )
                dagster_logger.info(f"{table_name} Successfully written to snowflake")
            else:
                dagster_logger.info(
                    "Did not match any file patterns in above logic. Skipping file"
                )
                dagster_logger.info(file)
    # clean up directory
    dagster_logger.info("Cleaning up directory now before completing")
    for root, dirs, files in os.walk(input_dir):
        for file in files:
            if not file.endswith((".zip", "accdb", ".xlsx", ".csv")):
                os.remove(os.path.join(root, file))
