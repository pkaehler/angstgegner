import os
import json

import click as click
import requests
import logging

from util.common import check_file_exists_in, save_json

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def download_data(url, headers, payload):
    logger.info(f'send request to {url}')
    response = requests.request("GET", url, headers=headers, data=payload)
    raw_leagues_format = json.loads(response.text)
    return raw_leagues_format


def _get_league_data(headers: dict, payload:dict):
    logger.info('Try to fetch league data')
    endpoint = f"leagues"
    filters = f"?"
    url = f"https://v3.football.api-sports.io/{endpoint}"
    storage_path = 'data/raw_leagues.json'
    if check_file_exists_in(storage_path):
        logger.info(f'File {storage_path} already exists.')
    else:
        data = download_data(url=url, headers=headers, payload=payload)
        if save_json(file_path=storage_path,file=data):
            logger.info(f'File saved to {storage_path}')


@click.command()
@click.option("--endpoint", help="endpoint to query (league,...)", type=str)
def get_data(endpoint: str):
    apikey = os.environ.get('FOOTBALL_COM_API')
    payload = {}
    headers = {
        'x-rapidapi-key': f'{apikey}',
        'x-rapidapi-host': 'v3.football.api-sports.io'
    }
    if endpoint == 'league':
        _get_league_data(headers=headers, payload=payload)
    else:
        logger.info(f'Not implemented yet: "{endpoint}"')


if __name__ == '__main__':
    get_data()