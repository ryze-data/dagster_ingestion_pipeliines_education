from dagster import (
    Definitions,
    EnvVar,
    ScheduleDefinition,
    FilesystemIOManager,
    define_asset_job,
    load_assets_from_modules,
)

from dagster_snowflake_pandas import SnowflakePandasIOManager
from dagster_snowflake import SnowflakeResource

from .assets.nces import nces_file_download, nces_snowflake_load
from .assets.s275 import s275_file_download, s275_snowflake_load


nces_download_assets = load_assets_from_modules([nces_file_download])
nces_load_assets = load_assets_from_modules([nces_snowflake_load])

s275_download_assets = load_assets_from_modules([s275_file_download])
s275_load_assets = load_assets_from_modules([s275_snowflake_load])


defs = Definitions(
    assets=[*nces_download_assets, *nces_load_assets,
            *s275_download_assets, *s275_load_assets],
    resources={
        "sf_io_manager": SnowflakePandasIOManager(
            # Read about using environment variables and secrets in Dagster:
            # https://docs.dagster.io/guides/dagster/using-environment-variables-and-secrets
            account=EnvVar("SNOWFLAKE_ACCOUNT"),
            user=EnvVar("SNOWFLAKE_USER"),
            password=EnvVar("SNOWFLAKE_PASSWORD"),
            warehouse=EnvVar("SNOWFLAKE_WAREHOUSE"),
            database=EnvVar("SNOWFLAKE_DATABASE"),
            schema=EnvVar("SNOWFLAKE_SCHEMA"),
        ),
        "fs_io_manager": FilesystemIOManager(),
        "snowflake": SnowflakeResource(
            # Read about using environment variables and secrets in Dagster:
            # https://docs.dagster.io/guides/dagster/using-environment-variables-and-secrets
            account=EnvVar("SNOWFLAKE_ACCOUNT"),
            user=EnvVar("SNOWFLAKE_USER"),
            password=EnvVar("SNOWFLAKE_PASSWORD"),
            warehouse=EnvVar("SNOWFLAKE_WAREHOUSE"),
            database=EnvVar("SNOWFLAKE_DATABASE"),
            schema=EnvVar("SNOWFLAKE_SCHEMA"),
        ),
    },
    # schedules=[daily_refresh_schedule],
)
