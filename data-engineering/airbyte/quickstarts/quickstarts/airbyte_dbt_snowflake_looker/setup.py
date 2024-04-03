from setuptools import find_packages, setup

setup(
    name="airbyte-dbt-snowflake-looker",
    packages=find_packages(),
    install_requires=[
        "dbt-snowflake",
        "dagster",
        "dagster-cloud",
        "dagster-dbt",
        "dagster-airbyte",
    ],
    extras_require={"dev": ["dagit", "pytest"]},
)