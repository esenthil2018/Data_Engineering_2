import pandas as pd
import sqlite3

# Extract
data = pd.read_excel("SRDataEngineerChallenge_DATASET.xlsx")

# Transform
data['full_name'] = data['first_name'] + " " + data['last_name']
data['email_domain'] = data['email'].str.split('@').str[1]

# Load
conn = sqlite3.connect('etl_database.db')
data.to_sql('users', conn, if_exists='replace', index=False)

# Optional: Print a message to indicate successful completion
print("ETL process completed successfully!")


