import requests
from google.cloud import storage
import json


def upload_json_to_bucket(storage_client, bucket_name, blob_name, file_name):
    try:
        bucket = storage_client.get_bucket(bucket_name)
        blob = bucket.blob(blob_name)
        blob.upload_from_string(
            data=json.dumps(file_name, indent=1),
            content_type='application/json'
        )

        return "successfully uploaded to {}".format(blob_name)
    
    except Exception as e:
        return "error: {}".format(e)


def request_api(url: str, header: dict, parameters:dict=None):
    try:
        r = requests.get(
            url,
            headers=header,
            params=parameters
        )

        return r.json()
    except Exception as e:
        return e
    
