"""
This file has variables you want to give assets to. Only non-sensitive variables
"""

# TODO: change this to use files stored here:
DOWNLOAD_DIRECTORY = "C:/Users/computer/src/github/ryze-data/dagster_ingestion_pipelines_education/dagster_ingestion_pipelines/dagster_ingestion_pipelines/data/s275/raw"
# Current websites as of 2024-02-02 https://ospi.k12.wa.us/safs-data-files

# the amount of time the pipeline will wait until starting new batch. This solves server timeout errors
# i.e. Server Connection Broke Error
BATCH_WAIT_TIME_SECONDS = 60

# Access Files. Splitting apart to avoid connection break error

# Excel Files
S275_URLS_BATCH_1 = [
    # 2023 - 2020
    "https://ospi.k12.wa.us/sites/default/files/2023-10/2022-2023_final_s-275_personnel_database_1.zip",
    "https://ospi.k12.wa.us/sites/default/files/2023-11/2021-2022_final_s-275_personnel_database.zip",
]

S275_URLS_BATCH_2 = [
    "https://ospi.k12.wa.us/sites/default/files/2023-08/2020-2021_final_s-275_personnel_database.zip",
    "https://ospi.k12.wa.us/sites/default/files/2023-08/2019-2020_final_s-275_personnel_database.zip",
]

S275_URLS_BATCH_3 = [
    # 2019
    "https://ospi.k12.wa.us/sites/default/files/2023-08/2018-2019_final_s-275_personnel_database.zip"
]

S275_URLS_BATCH_4 = [
    # 2018
    "https://ospi.k12.wa.us/sites/default/files/2023-08/2017-2018finals-275personneldatabase.zip",
    "https://ospi.k12.wa.us/sites/default/files/2023-08/2016-2017_final_s-275_personnel_database.zip",
]

S275_URLS_BATCH_5 = [
    # 2016
    "https://ospi.k12.wa.us/sites/default/files/2023-08/2015-2016_final_s-275_personnel_database.zip",
]

S275_URLS_BATCH_6 = [
    # 2015
    "https://ospi.k12.wa.us/sites/default/files/2023-08/2014-2015_final_s-275_personnel_database.zip",
    "https://ospi.k12.wa.us/sites/default/files/2023-08/2013-2014_final_s-275_personnel_database.zip",
]

# union of all column names found across files for all years.
# we list these explicitly here to eliminate variations in column order;
# this way, we can import all flat files into a single table
ALL_POSSIBLE_COLUMNS = [
    "SchoolYear",
    "area",
    "cou",
    "dis",
    "codist",
    "LastName",
    "FirstName",
    "MiddleName",
    "lname",
    "fname",
    "mname",
    "cert",
    "bdate",
    "byr",
    "bmo",
    "bday",
    "sex",
    "ethnic",
    "hispanic",
    "race",
    "hdeg",
    "hyear",
    "acred",
    "icred",
    "bcred",
    "vcred",
    "exp",
    "camix",
    "camix1",
    "camix1A",
    "camix1S",
    "camix1Sa",
    "camix1SB",
    "ftehrs",
    "ftedays",
    "certfte",
    "clasfte",
    "certbase",
    "clasbase",
    "othersal",
    "tfinsal",
    "cins",
    "cman",
    "cbrtn",
    "clasflag",
    "certflag"
    # metadata field, probably for district-level columns. this is useful for tracking.
    ,
    "ceridate"
    # don't know what this is, there's already a camix1
    # ,"camix1S"
    ,
    "NBcertexpdate",
    "recno"
    # always NULL in the files
    # ,"parea"
    ,
    "prog",
    "act",
    "darea",
    "droot",
    "dsufx",
    "grade",
    "bldgn",
    "asspct",
    "assfte",
    "asssal",
    "asshpy",
    "major"
    # metadata field, probably for assignment-level columns. this is useful for tracking.
    ,
    "crasdate",
    "yr",
]
