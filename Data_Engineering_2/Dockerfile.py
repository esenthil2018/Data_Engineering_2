FROM python:3.8-slim

# Set a working directory
WORKDIR /app

# Install necessary libraries
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy ETL script and dataset
COPY etl_script.py etl_script.py
COPY SRDataEngineerChallenge_DATASET.xlsx SRDataEngineerChallenge_DATASET.xlsx

# Command to run the ETL script
CMD ["python", "etl_script.py"]


