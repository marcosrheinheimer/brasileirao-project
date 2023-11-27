import os
import requests
from dotenv import load_dotenv, find_dotenv

from google.cloud import storage


def upload_blob_from_memory(bucket_name, contents, destination_blob_name):
    """Uploads a file to the bucket."""

    # The ID of your GCS bucket
    # bucket_name = "your-bucket-name"

    # The contents to upload to the file
    # contents = "these are my contents"

    # The ID of your GCS object
    # destination_blob_name = "storage-object-name"

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_string(contents)

    print(
        f"{destination_blob_name} with contents {contents} uploaded to {bucket_name}."
    )


def request_api(url: str, header: dict):
    try:
        r = requests.get(
            url,
            headers=header,
            params=param
        )

        return r.json()
    except Exception as e:
        return e
    

if __name__ == '__main__':
    load_dotenv(find_dotenv())
    
    header = {
        'X-RapidAPI-Key': os.getenv('RAPID_API_KEY'),
        'X-RapidAPI-Host': os.getenv('RAPID_API_HOST')
    }

    param = {
        'country': 'Brazil'
    }

    leagues = request_api('https://api-football-v1.p.rapidapi.com/v3/leagues', header)
    
    # Send to Storage
    bucket_name = os.getenv('GCP_BUCKET_NAME')
    destination_name = 'test.json'

    upload_blob_from_memory(bucket_name, leagues, destination_name)

