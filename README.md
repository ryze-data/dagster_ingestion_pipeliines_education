# Dagster Ingestion Pipelines - Education Examples

This holds s275 and NCES pipelines

## Getting started

### Requirements

- Windows 10 (What this was tested on)
- Commands executed in Powershell. NOT command prompt.
- Python = 3.10.0 (Python 3.11 is supported as well)
    - ONLY one version of python that is in the Environment Variable path (any confusion of python can produce unexpected errors)

- Assumptions are that this repository is installed in your home directory

### Recommended: Virtual Environment

- This assumes you are using Windows and that python was installed from the microsoft store

0. Download repo (optional)

**Commands below created for powershell**

```
$url = "https://github.com/ryze-data/dagster_ingestion_pipelines_education/archive/refs/heads/main.zip"
$output = "$HOME\dagster_nces-main.zip"
$extractPath = "$HOME"
Invoke-WebRequest -Uri $url -OutFile $output
Expand-Archive -Path $output -DestinationPath $extractPath
Remove-Item $output  # Optional: Remove the downloaded ZIP file after extraction
```

1. Navigate to project

```bash
# rename the project
Rename-Item $HOME\dagster_ingestion_pipelines_education-main dagster_ingestion_pipelines_education
# to be executed in powershell
cd $HOME\dagster_ingestion_pipelines_education
```

2. Create Virtual Environment

```bash
# to be executed inside the project directory
# powershell
python -m venv venv_dagster
```
3. Activate Virtual Environment

```bash
.\venv_dagster\Scripts\activate
```

```bash
# this can be run if you want to make sure you have the latest version of pip
python -m pip install --upgrade pip
```

4. Deactivate Virtual Environment (Only when trying to leave virtual environment)

```bash
# When you want to opt out of Virtual Environment 
deactivate
```

### Installation

First, install your Dagster code location as a Python package. By using the --editable flag, pip will install your Python package in ["editable mode"](https://pip.pypa.io/en/latest/topics/local-project-installs/#editable-installs) so that as you develop, local code changes will automatically apply.

```bash
# change to directory with project.toml
cd .\dagster_ingestion_pipelines\  
# install dependencies
pip install -e ".[dev]"
```

In the same directory as the pyproject.toml, create a .env file with the snowflake credentials:
```
# example of .env file
SNOWFLAKE_ACCOUNT="insert_here"
SNOWFLAKE_USER="insert_here"
SNOWFLAKE_PASSWORD="insert_here"
SNOWFLAKE_DATABASE="insert_here"
SNOWFLAKE_WAREHOUSE="insert_here"
SNOWFLAKE_SCHEMA="insert_here"
```

Then, start the Dagster UI web server:

```bash
dagster dev
```


Open http://localhost:3000 with your browser to see the project.

You can start writing assets in `dagster_ingestion_pipelines/assets` directory with the @asset decorator. The assets are automatically loaded into the Dagster code location as you define them.

**GLOBAL variables will be found in the `dagster_ingestion_pipelines/assets/nces/constants.py` or `dagster_ingestion_pipelines/assets/s275/constants.py` file. You will need to change the filepath of where you want the data written to.**

### Where should I put my credential information snowflake?

The simplest way is by using the .env file in the same folder the pyproject.toml file is in. Or you can set in Windows Server. Notice in the `dagster_ingestion_pipelines/__init__.py__` I specify resource, job, asset etc. defintions.


## Development

### Adding new Python dependencies

You can specify new Python dependencies in `setup.py`.

### Unit testing

No tests were implemented for this project. However Tests are in the `dagster_ingestion_pipelines_tests` directory and you can run tests using `pytest`:

```bash
pytest dagster_ingestion_pipelines
```

### Schedules and sensors

If you want to enable Dagster [Schedules](https://docs.dagster.io/concepts/partitions-schedules-sensors/schedules) or [Sensors](https://docs.dagster.io/concepts/partitions-schedules-sensors/sensors) for your jobs, the [Dagster Daemon](https://docs.dagster.io/deployment/dagster-daemon) process must be running. This is done automatically when you run `dagster dev`.

Once your Dagster Daemon is running, you can start turning on schedules and sensors for your jobs.


## More info

### NCES

Some of this repo orchestrates pulling data from a public school website and uploading to snowflake with dagster [NCES Common Core of Data set](https://nces.ed.gov/ccd/) of archival files (2001 - present)

This project came from the following link:  https://github.com/CCER-RMP/NCES

### S275

Some of this repo pulls [WA State S-275 school personnel data](https://ospi.k12.wa.us/safs-data-files) from the [Washington Office of Superintendent of Public Instruction (OSPI)](https://ospi.k12.wa.us/) website. This project came from the following link: https://github.com/CCER-RMP/S275_ETL