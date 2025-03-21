# Lecture code snippets

I will use this file to mention installation requirements for lecture demos and also any code snippets that I will be copy/pasting during the lecture demo.

## Fri, Mar 21 (Data Transformation):

dbt (Data Build Tool) is an open-source command-line tool used by data teams to transform raw data into a clean, analytical format within a data warehouse. It enables data analysts and engineers to build, test, and document data models through SQL scripts. 

### dbt installation

- All of the following installations will be in your GCP VM. Make sure that you bring down the elasticsearch docker cluster. If you run into disk space issues, please make sure to delete unnecessary files. 
- First install miniconda following the instruction [here](https://www.anaconda.com/docs/getting-started/miniconda/install#macos-linux-installation). Go ahead and enter "yes" for this question "Do you wish to update your shell profile to automatically initialize conda?".
- Then create a miniconda env named `p4-env` using `conda create -n p4-env python=3.10`. All the packages will be installed in the new envs and will not interrupt your base env. It will be very useful when you are having multiple projects on your VM.
- Make sure to close your ssh session and open a new session.
- Then activate your conda environment using `conda activate p4-env`.
- Finally, install the required modules
```
pip install snowflake-connector-python dbt-snowflake dbt-core pandas matplotlib sqlalchemy snowflake-sqlalchemy
```

### dbt configuration steps:

- Configure `profiles.yml` for Snowflake:

```
mkdir ~/.dbt
touch ~/.dbt/profiles.yml
```

- dbt initialize a new dbt project

```
dbt init p4_survey_pipeline
```
  - When you run dbt init <project_name>, it creates a directory with the specified project name. Inside this directory, it sets up the default project structure, which includes:
    - models/: This is where your dbt models (SQL queries) are stored.
    - seeds/: This is where CSV files are placed that you want to load into your data warehouse.
    - tests/: This is where you can store data tests.
    - macros/: This is where you store reusable SQL functions and macros.
    - analysis/: This is where you can store analysis queries.
    - data/: Directory for the data files.
    - target/: This folder is where dbt stores the results of runs (compiled SQL files, logs, etc.), but this folder is typically ignored in version control.
    - logs/: This is where dbt writes its logs during execution.
    - dbt_project.yml: The main configuration file that holds project-specific configurations like project name, version, models configurations, etc.
    - profiles.yml (optional but recommended): dbt will suggest that you set up a connection to your data warehouse.

- Define the Source Table in dbt:
```
cd p4_survey_pipeline
vim models/schema.yml
```

- Create a dbt Model to apply necessary transformations

```
mkdir models/staging
vim models/staging/transform_survey.sql
```
- Check status of dbt connection
```
dbt debug  # check if dbt is correctly connected to Snowflake 
```
- Apply dbt transformations
```
dbt run
dbt run --target other
```

## Wed, Mar 19 (Data Pipeline):

- In your VM, install Snowflake connector. You should already have pandas and matplotlib installed, but just in case you provisioned a new VM, I am listing those as well.
```
pip install snowflake-connector-python pandas matplotlib
```

## Airbyte free trial

- You need to register an Airbyte web version account at https://airbyte.com/ and claim your 14-day free trial for Airbyte using your personal email.
  - **IMPORTANT**: I am asking you to create trial with your personal email because you will run out of free-trial period prior to the deadline. For project p4, please make sure to create another account with your wisc.edu email.

## Snowflake free trial

- You need to register a Snowflake web account at https://www.snowflake.com/en/ and claim your 30-day free trial. Since it is a 30-day trial, you can sign up directly using your wisc.edu email.

## Wed, Mar 5 (ElasticSearch):

## Upgrade your VM to e2-medium 
- Stop and remove all running `docker` containers.
- Remove all extra/unnecessary data files. You can always redownload when you want to review those topics.
- We'll continue to have disk size as 25GB.
- Here's a helpful [tutorial](https://cloud.google.com/compute/docs/instances/changing-machine-type-of-stopped-instance) to upgrade your existing VM.
- **IMPORTANT**: It is very important that you go through this step first before you go through the installation for ElasticSearch. Otherwise, the installation might fail!

## Setting up ElasticSearch using Docker

**Note** Developing in VS Code is way easier! (The extension: Remote-SSH is a life saver). Please consider switching to VS code instead of 10 floating terminals.

- In your VM, install Elastisearch and Kibana (with docker):
```bash
curl -fsSL https://elastic.co/start-local | sh
```

**This command will give you a password and an API key as shown below. Store both.**

![output_of_installing_elasticsearch_with_docker](output_local_install.png)

- To restart your container, cd into `elastic-search-local`: 
```bash
docker stop es-local-dev
cd elastic-start-local
docker compose up -d
```

Sometimes you have to remove the elastic-start-local dir and start from scratch (container state becomes unhealthy when you re-start your VM sometimes)

- [Optional] Sanity check your elasticsearch connection. In your VM:
```bash
cd elastic-start-local
source .env
curl $ES_LOCAL_URL -H "Authorization: ApiKey ${ES_LOCAL_API_KEY}"
```

---

## Setting up `jupyter` and `python elasticsearch-client`

- Install `elasticsearch` so we can interact with elasticsearch via Python.

```bash
pip3 install elasticsearch
```


## Wed, Feb 19 (MongoDB):

#### Installations on your VM:

```
pip3 install jupyter pandas nbformat nbconvert
pip3 install pymongo 
pip3 install geopandas matplotlib
```

#### Docker clean up

```
docker system prune
docker rm `docker ps -aq`
docker rmi -f `docker images -aq` (force removes stale images)
```
```
docker pull mongo
docker run --name <container-name> -d -p 127.0.0.1:27017:27017 mongo
```
```
docker exec -it <CONTAINER NAME> bash
```

--------------------------------

## Mon, Feb 3 (MySQL):

#### Installations on your VM:

Optional: Stop your VM, refresh your window after a few minutes, and “Start / Resume” to update kernel version

``` 
sudo apt-get update
sudo apt-get install python3-pip wget unzip
```
```
sudo pip3 install jupyter
pip3 install SQLAlchemy mysql-connector-python pandas
pip3 install pandas
```

#### Docker clean up

```
docker system prune
docker rm `docker ps -aq`
docker rmi -f `docker images -aq` (force removes stale images)
```
```
docker pull mysql
docker run -d -m "1g" -p 127.0.0.1:3306:3306 -e MYSQL_DATABASE=cs639 -e MYSQL_ROOT_PASSWORD=abc mysql
```
```
docker exec -it \<CONTAINER NAME\> bash
```

```
mysql -p cs639
help
show tables;

git pull (inside your s25 directory)
# Note: navigate to today's lecture directory within your s25 directory
jupyter notebook
```

#### Establish ssh tunnel (from your laptop to your VM):

**IMPORTANT NOTE:** You need to open a new terminal / powershell tab on your laptop to establish this ssh tunnel.

```
ssh USER@<IP> -L localhost:8888:localhost:8888
```
