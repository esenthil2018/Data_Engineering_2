Data Engineering ETL Challenge
This repository contains the ETL (Extract, Transform, Load) solution for the Deloitte Challenge.

Overview
The project aims to ingest data from a provided dataset, transform it by creating additional fields based on the existing data, and load it into a SQLite database.

Setup
Prerequisites
Docker
Docker Compose

Running the ETL
git clone https://github.com/esenthil2018/Data_Engineering_2.git
cd Data_Engineering_2

Build and run the Docker container:
docker-compose up --build

Once the container is running, the ETL script will automatically start processing the data.

ETL Process
Extraction: Data is extracted from the provided SRDataEngineerChallenge_DATASET.xlsx file.
Transformation:
New fields are created based on the existing data.
Data cleaning and validation is performed.
Loading: The transformed data is loaded into a SQLite database.
Technologies Used
Python
Pandas
SQLite
Docker

