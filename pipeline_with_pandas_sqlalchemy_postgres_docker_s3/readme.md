# Example Pipeline for Club 100 Companies Data Pipeline Exercise

This is an example of a data pipeline architecture to generate fake data for Ghana Club 100 companies and ingest it into a database.

## Instructions

These instructions will help guide any user to test out this data pipeline.

### Requirements

- [Python v3.7+](https://www.python.org/downloads/)
- [Docker Desktop v25.0+](https://docs.docker.com/desktop/)
- [AWS S3 Read/Write Access](https://aws.amazon.com/pm/serv-s3/)

### Installation

1. Make sure all the requirements are set up correctly. Follow the provided links to download and install the required software and set up an AWS user with access to the S3 service.

2. Open the current directory (`pipeline_with_pandas_sqlalchemy_postgres_docker_s3`) in a terminal window that has access to your python and docker installation. If you cloned the entire repo, you can `cd ./pipeline_with_pandas_sqlalchemy_postgres_docker_s3` into the correct directory.

3. (Optional) You may want to create a python virtual environment to isolate project dependencies from your system dependencies. See [here](https://docs.python.org/3/library/venv.html) for help with doing that. Activate the virtual environment after creating it.

4. Run `python -m pip install -r requirements.txt` to install the project dependencies.

### Running the pipeline

1. Generate the data needed for the pipeline by running the `<company_name>_data_generator.py` scripts. For example, run `abosso_goldfields_limited_data_generator.py` to generate data for `abosso_goldfields_limited`.

2. In order not to clutter the Github repository with large CSV files, persist the generated data on S3 and remember to exclude the data directory from your source tree. For detailed instructions on persisting on S3, reference `s3_scripts_readme.md`.

3. Run `python ./initdb/initsql.py` to create the database initialization script. This script creates databases for all the companies whose data exist in the data directory. If you added any CSV files manually to the data directory, make sure they are in the correct logical structure: `./data/<company_name>/table_name.csv`.

4. (Optional) You may want to set up some environment variables for the docker containers. Look up how to set environment variables for your operating system if you are having trouble achieving that.

   ```environment variables
   POSTGRES_USERNAME
   POSTGRES_PASSWORD
   PGADMIN_DEFAULT_EMAIL
   PGADMIN_DEFAULT_PASSWORD
   ```

5. Make sure your docker daemon is up and running. Then run `docker compose up --build` to spin up the compose stack. The stack is made up of the pipeline ingestion python application, a PostgreSQL server, and a PGAdmin4 server.

6. Open [http://localhost:1111](http://localhost:1111) to access the PGAdmin web interface and connect to your databases. Login with the PGADMIN_DEFAULT_EMAIL and PGADMIN_DEFAULT_PASSWORD environment values you set in the previous step. If you did not set the environment variables, type `francis@trestleacademyghana.org` as the email and `secret` as the password.

7. Connect to the postgres server with service name as `db`, user name as POSTGRES_USERNAME or `postgres` and password as POSTGRES_PASSWORD or `postgres`. You should now be able to access the data you that was ingested.

### Answering some analytics questions

1. Refer to `analytics_queries_<company_name>.md` for 10 questions and sql queries that can answer them. For example, open `analytics_queries_abosso_goldfields_limited.md`, copy the queries and run them in PGADMIN to answer the corresponding question.

## Contributors

- [Francis Echesi](https://github.com/FrankE01)
