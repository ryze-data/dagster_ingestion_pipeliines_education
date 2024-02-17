from setuptools import find_packages, setup

setup(
    name="s275_pipeline",
    packages=find_packages(exclude=["s275_pipeline_tests"]),
    install_requires=[
        "dagster",
        "pyodbc",
        "requests",
        "openpyxl",
        "pandas",
        "snowflake-connector-python[pandas]",
        "dagster-snowflake-pandas",
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
