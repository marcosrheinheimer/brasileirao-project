from brasileirao-project.extract-load import gcp-resources
from dotenv import load_dotenv, find_dotenv
import os
import requests
import json

from gcp


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
    leagues

