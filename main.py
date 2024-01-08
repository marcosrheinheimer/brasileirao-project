from extract_load.extract import upload_json_to_bucket, request_api
import os
import dotenv
import json

from google.cloud import storage

dotenv.load_dotenv()
header = {
        'X-RapidAPI-Key': os.getenv('RAPID_API_KEY'),
        'X-RapidAPI-Host': os.getenv('RAPID_API_HOST')
}

param = {
        'country': 'Brazil'
}

leagues = request_api('https://api-football-v1.p.rapidapi.com/v3/leagues', header, param)

# Sending to GCP Bucket
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'gcp_storage_credentials.json'
stg_client = storage.Client()

upload_json_to_bucket(stg_client, 'stg-brasileirao-raw', 'leagues2', leagues)


