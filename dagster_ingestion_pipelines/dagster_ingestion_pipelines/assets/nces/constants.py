"""
This file has variables you want to give assets to. Only non-sensitive variables
"""

# TODO: change this to use files stored on S:
# DOWNLOAD_DIR = "S:/Data/Data System/RawSourceFiles/NCES/Common Core of Data"
DOWNLOAD_DIRECTORY = "C:/Users/computer/src/github/ryze-data/dagster_ingestion_pipelines_education/dagster_ingestion_pipelines/dagster_ingestion_pipelines/data/nces/raw"


####### NCES - Common Core of Data ########
# from 2015 to 2018, there are 5 files in common core, and a separate geocode file

# these are school-level files

# to find these files via the website, go to this URL:
# https://nces.ed.gov/ccd/files.asp
# select 'Nonfiscal' and 'School' for the level.
# the geocode files is separate:
# https://nces.ed.gov/programs/edge/Geographic/SchoolLocations

# three-char codes in the filenames:
# 029 = directory file
# 052 = membership file
# 059 = staff file
# 129 = school characteristics file
# 033 = lunch program accessibility

NCES_URLS_BATCH_1 = [
    # 2022
    "https://nces.ed.gov/ccd/Data/zip/ccd_sch_029_2122_w_1a_071722.zip",
    "https://nces.ed.gov/ccd/Data/zip/ccd_SCH_052_2122_l_1a_071722.zip",
    "https://nces.ed.gov/ccd/Data/zip/ccd_sch_059_2122_l_1a_071722.zip"

]

NCES_URLS_BATCH_2 = [

    "https://nces.ed.gov/ccd/Data/zip/ccd_sch_129_2122_w_1a_071722.zip",
    "https://nces.ed.gov/ccd/Data/zip/ccd_sch_033_2122_l_1a_071722.zip"
    # geocode
    ,
    "https://nces.ed.gov/programs/edge/data/EDGE_GEOCODE_PUBLICSCH_2122.zip"
    # postsecondary geocode
    ,
    "https://nces.ed.gov/programs/edge/data/EDGE_GEOCODE_POSTSECONDARYSCH_2122.zip",
]

NCES_URLS_BATCH_3 = [
    # 2021
    "https://nces.ed.gov/ccd/Data/zip/ccd_sch_029_2021_w_1a_080621.zip",
    "https://nces.ed.gov/ccd/Data/zip/ccd_sch_052_2021_l_1a_080621.zip",
    "https://nces.ed.gov/ccd/Data/zip/ccd_sch_059_2021_l_1a_080621.zip",
    "https://nces.ed.gov/ccd/Data/zip/ccd_sch_129_2021_w_1a_080621.zip",
    "https://nces.ed.gov/ccd/Data/zip/ccd_sch_033_2021_l_1a_080621.zip"
    # geocode
    ,
    "https://nces.ed.gov/programs/edge/data/EDGE_GEOCODE_PUBLICSCH_2021.zip"
    # postsecondary geocode
    ,
    "https://nces.ed.gov/programs/edge/data/EDGE_GEOCODE_POSTSECONDARYSCH_2021.zip",
]

NCES_URLS_BATCH_4 = [

    "https://nces.ed.gov/ccd/Data/zip/ccd_sch_129_2021_w_1a_080621.zip",
    "https://nces.ed.gov/ccd/Data/zip/ccd_sch_033_2021_l_1a_080621.zip"
    # geocode
    ,
    "https://nces.ed.gov/programs/edge/data/EDGE_GEOCODE_PUBLICSCH_2021.zip"
    # postsecondary geocode
    ,
    "https://nces.ed.gov/programs/edge/data/EDGE_GEOCODE_POSTSECONDARYSCH_2021.zip",
]

NCES_URLS_BATCH_5 = [
    # 2020
    "https://nces.ed.gov/ccd/Data/zip/ccd_sch_029_1920_w_1a_082120.zip",
    "https://nces.ed.gov/ccd/Data/zip/ccd_SCH_052_1920_l_1a_082120.zip",
    "https://nces.ed.gov/ccd/Data/zip/ccd_sch_059_1920_l_1a_082120.zip",
    "https://nces.ed.gov/ccd/Data/zip/ccd_sch_129_1920_w_1a_082120.zip",
    "https://nces.ed.gov/ccd/Data/zip/ccd_sch_033_1920_l_1a_082120.zip"
    # geocode
    ,
    "https://nces.ed.gov/programs/edge/data/EDGE_GEOCODE_PUBLICSCH_1920.zip"
    # postsecondary geocode
    ,
    "https://nces.ed.gov/programs/edge/data/EDGE_GEOCODE_POSTSEC_1920.zip",
]

NCES_URLS_BATCH_6 = [
    # 2019
    "https://nces.ed.gov/ccd/data/zip/ccd_sch_029_1819_w_1a_091019.zip",
    "https://nces.ed.gov/ccd/data/zip/ccd_sch_052_1819_l_1a_091019.zip",
    "https://nces.ed.gov/ccd/data/zip/ccd_sch_059_1819_l_1a_091019.zip",
    "https://nces.ed.gov/ccd/data/zip/ccd_sch_129_1819_w_1a_091019.zip",
    "https://nces.ed.gov/ccd/data/zip/ccd_sch_033_1819_l_1a_091019.zip"
    # geocode
    ,
    "https://nces.ed.gov/programs/edge/data/EDGE_GEOCODE_PUBLICSCH_1819.zip"
    # postsecondary geocode
    ,
    "https://nces.ed.gov/programs/edge/data/EDGE_GEOCODE_POSTSECONDARYSCH_1819.zip"
    # 2018
    ,
    "https://nces.ed.gov/ccd/Data/zip/ccd_sch_029_1718_w_1a_083118.zip",
    "https://nces.ed.gov/ccd/Data/zip/ccd_sch_052_1718_l_1a_083118.zip",
    "https://nces.ed.gov/ccd/Data/zip/ccd_sch_059_1718_l_1a_083118.zip",
    "https://nces.ed.gov/ccd/Data/zip/ccd_sch_129_1718_w_1a_083118.zip",
    "https://nces.ed.gov/ccd/Data/zip/ccd_sch_033_1718_l_1a_083118.zip"
    # geocode
    ,
    "https://nces.ed.gov/programs/edge/data/EDGE_GEOCODE_PUBLICSCH_1718.zip"
    # postsecondary geocode
    ,
    "https://nces.ed.gov/programs/edge/data/EDGE_GEOCODE_POSTSECONDARYSCH_1718.zip",
]

NCES_URLS_BATCH_7 = [
    # 2017
    "https://nces.ed.gov/ccd/Data/zip/ccd_sch_029_1617_w_1a_11212017_csv.zip",
    "https://nces.ed.gov/ccd/Data/zip/ccd_SCH_052_1617_l_2a_11212017_CSV.zip",
    "https://nces.ed.gov/ccd/Data/zip/ccd_sch_059_1617_l_2a_11212017_csv.zip",
    "https://nces.ed.gov/ccd/Data/zip/ccd_sch_129_1617_w_1a_11212017_csv.zip",
    "https://nces.ed.gov/ccd/Data/zip/ccd_sch_033_1617_l_2a_11212017_csv.zip"
    # geocode
    ,
    "https://nces.ed.gov/programs/edge/data/EDGE_GEOCODE_PUBLICSCH_1617.zip"
    # postsecondary geocode
    ,
    "https://nces.ed.gov/programs/edge/data/EDGE_GEOCODE_POSTSECONDARYSCH_1617.zip"
    # 2016
    ,
    "https://nces.ed.gov/ccd/Data/zip/ccd_sch_029_1516_w_2a_011717_csv.zip",
    "https://nces.ed.gov/ccd/Data/zip/ccd_sch_052_1516_w_2a_011717_csv.zip",
    "https://nces.ed.gov/ccd/Data/zip/ccd_sch_059_1516_w_2a_011717_csv.zip",
    "https://nces.ed.gov/ccd/Data/zip/ccd_sch_129_1516_w_2a_011717_csv.zip",
    "https://nces.ed.gov/ccd/Data/zip/ccd_sch_033_1516_w_2a_011717_csv.zip"
    # geocode
    ,
    "https://nces.ed.gov/programs/edge/data/EDGE_GEOCODE_PUBLICSCH_1516.zip"
    # postsecondary geocode
    ,
    "https://nces.ed.gov/programs/edge/data/EDGE_GEOCODE_POSTSECONDARYSCH_1516.zip",
]

NCES_URLS_BATCH_8 = [

    # 2015
    "https://nces.ed.gov/ccd/Data/zip/ccd_sch_029_1415_w_0216601a_txt.zip",
    "https://nces.ed.gov/ccd/Data/zip/ccd_sch_052_1415_w_0216161a_txt.zip",
    "https://nces.ed.gov/ccd/Data/zip/ccd_sch_059_1415_w_0216161a_txt.zip",
    "https://nces.ed.gov/ccd/Data/zip/ccd_sch_129_1415_w_0216161a_txt.zip",
    "https://nces.ed.gov/ccd/Data/zip/ccd_sch_033_1415_w_0216161a_txt.zip"
    # last year that geocode data is provided as part of common core data; after this, it's on EDGE page
    ,
    "https://nces.ed.gov/ccd/Data/zip/EDGE_GEOIDS_201415_PUBLIC_SCHOOL_csv.zip"
    # 2014
    ,
    "https://nces.ed.gov/ccd/Data/zip/sc132a_txt.zip"
    # 2013
    ,
    "https://nces.ed.gov/ccd/Data/zip/sc122a_txt.zip"
    # 2012
    ,
    "https://nces.ed.gov/ccd/Data/zip/sc111a_supp_txt.zip"
    # 2011
    ,
    "https://nces.ed.gov/ccd/Data/zip/sc102a_txt.zip"
    # 2010
    ,
    "https://nces.ed.gov/ccd/data/zip/sc092a_txt.zip"
    # 2009
    ,
    "https://nces.ed.gov/ccd/data/zip/sc081b_txt.zip"
    # 2008
    ,
    "https://nces.ed.gov/ccd/data/zip/sc071b_txt.zip"
    # 2007
    ,
    "https://nces.ed.gov/ccd/data/zip/sc061cai_dat.zip",
    "https://nces.ed.gov/ccd/data/zip/sc061ckn_dat.zip",
    "https://nces.ed.gov/ccd/data/zip/sc061cow_dat.zip"
    # 2006
    ,
    "https://nces.ed.gov/ccd/data/zip/sc051aai_dat.zip",
    "https://nces.ed.gov/ccd/data/zip/sc051akn_dat.zip",
    "https://nces.ed.gov/ccd/data/zip/sc051aow_dat.zip"
    # 2005
    ,
    "https://nces.ed.gov/ccd/data/zip/sc041bai_dat.zip",
    "https://nces.ed.gov/ccd/data/zip/sc041bkn_dat.zip",
    "https://nces.ed.gov/ccd/data/zip/sc041bow_dat.zip"
    # 2004
    ,
    "https://nces.ed.gov/ccd/data/zip/sc031aai_dat.zip",
    "https://nces.ed.gov/ccd/data/zip/sc031akn_dat.zip",
    "https://nces.ed.gov/ccd/data/zip/sc031aow_dat.zip"
    # 2003
    ,
    "https://nces.ed.gov/ccd/data/zip/sc021aai_dat.zip",
    "https://nces.ed.gov/ccd/data/zip/sc021akn_dat.zip",
    "https://nces.ed.gov/ccd/data/zip/sc021aow_dat.zip"
    # 2002
    ,
    "https://nces.ed.gov/ccd/data/zip/sc011aai_dat.zip",
    "https://nces.ed.gov/ccd/data/zip/sc011akn_dat.zip",
    "https://nces.ed.gov/ccd/data/zip/sc011aow_dat.zip"
    # 2001
    ,
    "https://nces.ed.gov/ccd/data/zip/sc001aai_dat.zip",
    "https://nces.ed.gov/ccd/data/zip/sc001akn_dat.zip",
    "https://nces.ed.gov/ccd/data/zip/sc001aow_dat.zip"
    # 2000
    ,
    "https://nces.ed.gov/ccd/data/zip/sc991bai_dat.zip",
    "https://nces.ed.gov/ccd/data/zip/sc991bkn_dat.zip",
    "https://nces.ed.gov/ccd/data/zip/sc991bow_dat.zip",
]

    # Convert geocode .xlsx files to .txt where .txt is not supplied
GEOCODECONVERT = [
        # public school
        (
            "EDGE_GEOCODE_PUBLICSCH_1516/EDGE_GEOCODE_PUBLICSCH_1516.xlsx",
            "EDGE_GEOCODE_PUBLICSCH_1516/EDGE_GEOCODE_PUBLICSCH_1516.txt",
        )
        # postsecondary
        ,
        ("EDGE_GEOCODE_POSTSECSCH_1819.xlsx", "EDGE_GEOCODE_POSTSECSCH_1819.txt"),
        ("EDGE_GEOCODE_POSTSECSCH_1718.xlsx", "EDGE_GEOCODE_POSTSECSCH_1718.txt"),
        (
            "EDGE_GEOCODE_POSTSECONDARYSCH_1617/EDGE_GEOCODE_POSTSECSCH_1617.xlsx",
            "EDGE_GEOCODE_POSTSECONDARYSCH_1617/EDGE_GEOCODE_POSTSECSCH_1617.txt",
        ),
        (
            "EDGE_GEOCODE_POSTSECONDARYSCH_1516/EDGE_GEOCODE_POSTSECONDARYSCH_1516.xlsx",
            "EDGE_GEOCODE_POSTSECONDARYSCH_1516/EDGE_GEOCODE_POSTSECONDARYSCH_1516.txt",
        ),
    ]

EDGE_GEOCODE_POSTSECSCH_COLUMNS = [
"UNITID"
,"INSTNM"
,"STREET"
,"CITY"
,"STATE"
,"ZIP"
,"STFIP"
,"CNTY"
,"NMCNTY"
,"LOCALE"
,"LAT"
,"LON"
,"CBSA"
,"NMCBSA"
,"CBSATYPE"
,"CSA"
,"NMCSA"
,"NECTA"
,"NMNECTA"
,"CD"
,"SLDL"
,"SLDU"
,"SCHOOLYEAR"
]

