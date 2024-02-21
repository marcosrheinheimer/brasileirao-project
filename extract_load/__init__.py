from extract_load.extract import upload_json_to_bucket, request_api
from extract_load.load import create_table_from_uri
import os
import dotenv
import json

from google.cloud import storage, bigquery

dotenv.load_dotenv()
header = {
        'X-RapidAPI-Key': os.getenv('RAPID_API_KEY'),
        'X-RapidAPI-Host': os.getenv('RAPID_API_HOST')
}

param = {
        'country': 'Brazil'
}

# Calling 
leagues = request_api('https://api-football-v1.p.rapidapi.com/v3/leagues', header, param)



# Getting Storage Client
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'gcp_storage_credentials.json'
stg_client = storage.Client()

# Sending to GCP Bucket
blob_obj = upload_json_to_bucket(stg_client, 'brasileirao-raw', 'leagues', leagues)
print(blob_obj)

# Creating Dataset
bq_client = bigquery.Client()
dataset = bq_client.create_dataset('api_football_raw')

create_table_from_uri('api_football_raw', 'leagues', 'gs://brasileirao-raw/leagues_newline.json')
