import os
import json
import requests
import logging

from util.common import check_file_exists_in

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def save_json(path: str, file) -> bool:
    try:
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(file, f)
        return True
    except Exception as e:
        logger.warning(f'Could not save file due to: {e}')
        return False


def download_data(url, headers, payload):
    logger.info(f'send request to {url}')
    response = requests.request("GET", url, headers=headers, data=payload)
    raw_leagues_format = json.loads(response.text)
    return raw_leagues_format


if __name__ == '__main__':
    apikey = os.environ.get('FOOTBALL_COM_API')
    endpoint = f"leagues"
    filters = f"?"
    url = f"https://v3.football.api-sports.io/{endpoint}"
    payload = {}
    headers = {
        'x-rapidapi-key': f'{apikey}',
        'x-rapidapi-host': 'v3.football.api-sports.io'
    }
    storage_path = 'data/raw_leagues.json'
    if check_file_exists_in(storage_path):
        logger.info(f'File {storage_path} already exists.')
    else:
        data = download_data(url=url, headers=headers, payload=payload)
        if save_json(path=storage_path,file=data):
            logger.info(f'File saved to {storage_path}')

