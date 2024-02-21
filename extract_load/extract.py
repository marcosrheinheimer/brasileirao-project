import requests
from google.cloud import storage
from google.api_core import exceptions
import json


def request_api(url: str, header: dict, parameters:dict=None):
    try:
        r = requests.get(
            url,
            headers=header,
            params=parameters
        )
        r.json()

        nld_json = [json.dumps(record) for record in json.load(r)]
        return nld_json
    except Exception as e:
        return e


def upload_json_to_bucket(storage_client, bucket_name, blob_name, file_name):
    try: 
        bucket = storage_client.get_bucket(bucket_name)

    except exceptions.Conflict:
        print('The {} bucket already exists').format(bucket_name)
    except exceptions.NotFound:
        storage_client.create_bucket(bucket_name)


    blob = bucket.blob(blob_name)
    blob.upload_from_string(
        data=json.dumps(file_name, indent=1),
            content_type='application/json'
    )

    return blob
    
