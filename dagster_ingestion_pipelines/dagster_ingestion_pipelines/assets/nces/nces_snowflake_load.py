"""
This asset module consists of loading nces Common Core of Data to Snowflake

This code was adopted from a git repo and modified a bit to function without errors
"""

import os  # used to navigate and perform operations on directories

import pandas as pd

from . import constants  # used to load common variables
from . import nces_file_download  # used to load common variables

from dagster import (
    get_dagster_logger,
    asset,
)  # used to load functions as assets by dagster
from dagster_snowflake import SnowflakeResource
from snowflake.connector.pandas_tools import write_pandas


@asset(deps=[nces_file_download.nces_ccd_files], group_name="NCES")
def snowflake_nces_raw_tables(snowflake: SnowflakeResource):
    dagster_logger = get_dagster_logger()
    # get directory
    input_dir = constants.DOWNLOAD_DIRECTORY

    # for each file in directory
    for root, dirs, files in os.walk(input_dir):
        for file in files:
            dagster_logger.info(f"Ingesting {file} file")
            table_name = os.path.basename(file).split(".")[0]
            # handle ccd_sch*.csv files
            if file.startswith("ccd_sch") and file.endswith(".csv"):
                path = os.path.join(root, file)
                df = pd.read_csv(f"{path}", dtype=str, encoding="latin1").astype(str)
                with snowflake.get_connection() as conn:
                    write_pandas(
                        conn,
                        df,
                        table_name.upper(),
                        auto_create_table=True,
                        overwrite=True,
                    )
            # handle ccd_sch*.txt files
            elif file.startswith("ccd_sch") and file.endswith(".txt"):
                path = os.path.join(root, file)
                df = pd.read_csv(
                    path, dtype=str, encoding="latin1", header=0, sep="\t"
                ).astype(str)
                dagster_logger.info(df.head())
                with snowflake.get_connection() as conn:
                    write_pandas(
                        conn,
                        df,
                        table_name.upper(),
                        auto_create_table=True,
                        overwrite=True,
                    )
            # handle .dat files
            elif file.endswith((".dat")):
                path = os.path.join(root, file)
                col_widths = [11, 8, 8, 10, 10, 10, 10, 10, 10, 10]
                df = pd.read_fwf(
                    path,
                    dtype=str,
                    encoding="latin1",
                    sep="\n",
                    index_col=0,
                    widths=col_widths,
                    names=None,
                )
                column_headers = [f"COLUMN{i+1}" for i in range(len(df.columns))]
                df.columns = column_headers
                dagster_logger.info(df.head())
                with snowflake.get_connection() as conn:
                    write_pandas(
                        conn,
                        df,
                        table_name.upper(),
                        auto_create_table=True,
                        overwrite=True,
                    )
            # handle EDGE_GEOCODE_POSTSEC*.txt files
            elif file.startswith("EDGE_GEOCODE_POSTSEC") and file.endswith(".txt"):
                path = os.path.join(root, file)
                df = pd.read_csv(
                    path, dtype=str, encoding="latin1", header=0, sep="|"
                ).astype(str)
                dagster_logger.info(df.head())
                with snowflake.get_connection() as conn:
                    write_pandas(
                        conn,
                        df,
                        table_name.upper(),
                        auto_create_table=True,
                        overwrite=True,
                    )

            elif file.startswith("EDGE_GEOCODE_POSTSEC") and file.endswith(".TXT"):
                path = os.path.join(root, file)
                df = pd.read_csv(
                    path, dtype=str, encoding="latin1", header=None, sep="|"
                ).astype(str)
                df.columns = constants.EDGE_GEOCODE_POSTSECSCH_COLUMNS
                dagster_logger.info(df.head())
                with snowflake.get_connection() as conn:
                    write_pandas(
                        conn,
                        df,
                        table_name.upper(),
                        auto_create_table=True,
                        overwrite=True,
                    )
            # handle EDGE_GEOCODE_PUBLIC files
            elif file.startswith("EDGE_GEOCODE_PUBLICSCH") and file.endswith(".TXT"):
                path = os.path.join(root, file)
                df = pd.read_csv(
                    path, dtype=str, encoding="latin1", header=None, sep="|"
                ).astype(str)
                dagster_logger.info(df.head())
                # for handling files with no column names
                column_headers = ["COLUMN" + str(i) for i in range(len(df.columns))]
                df.columns = column_headers
                with snowflake.get_connection() as conn:
                    write_pandas(
                        conn,
                        df,
                        table_name.upper(),
                        auto_create_table=True,
                        overwrite=True,
                    )
            elif file.startswith("EDGE_GEOCODE_PUBLICSCH") and file.endswith(".txt"):
                path = os.path.join(root, file)
                df = pd.read_csv(
                    path, dtype=str, encoding="latin1", header=0, sep="|"
                ).astype(str)
                dagster_logger.info(df.head())
                # for handling files with no column names
                column_headers = ["COLUMN" + str(i) for i in range(len(df.columns))]
                df.columns = column_headers
                with snowflake.get_connection() as conn:
                    write_pandas(
                        conn,
                        df,
                        table_name.upper(),
                        auto_create_table=True,
                        overwrite=True,
                    )
            # EDGE_GEOIDS files
            elif file.startswith("EDGE_GEOIDS_") and file.endswith(".TXT"):
                path = os.path.join(root, file)
                df = pd.read_csv(
                    path, dtype=str, encoding="latin1", header=None, sep="|"
                ).astype(str)
                dagster_logger.info(df.head())
                with snowflake.get_connection() as conn:
                    write_pandas(
                        conn,
                        df,
                        table_name.upper(),
                        auto_create_table=True,
                        overwrite=True,
                    )

            elif file.startswith("EDGE_GEOIDS_") and file.endswith(".csv"):
                path = os.path.join(root, file)
                df = pd.read_csv(
                    path, dtype=str, encoding="latin1", header=0, sep=","
                ).astype(str)
                dagster_logger.info(df.head())
                with snowflake.get_connection() as conn:
                    write_pandas(
                        conn,
                        df,
                        table_name.upper(),
                        auto_create_table=True,
                        overwrite=True,
                    )
            else:
                dagster_logger.info(
                    "Skipping file. Did not match any file patterns in above logic."
                )

            dagster_logger.info(f"{table_name} handled. Handling next file")
