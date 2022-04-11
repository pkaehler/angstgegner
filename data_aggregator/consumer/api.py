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
    raw_data = json.loads(response.text)
    return raw_data

def teams_endpoint() -> str:
    """
    returns query params
    """
    #https://v3.football.api-sports.io/teams?league=78&season=2021
    return "?/league=7&season=2021"


def _get_data_from(endpoint: str, headers: dict, payload: dict):
    endpoint = f"{endpoint}"
    mapper = {
        "": "",
        "teams": teams_endpoint()
    }
    url = f"https://v3.football.api-sports.io/{endpoint}/{mapper[endpoints]}"
    storage_path = f"data/raw_{endpoint}.json"
    logger.info('Try to fetch data from {}')
    if check_file_exists_in(storage_path):
        logger.info(f'Stopped. File {storage_path} already exists.')
    else:
        data = download_data(url=url, headers=headers, payload=payload)
        if save_json(file_path=storage_path, file=data):
            logger.info(f'File saved to {storage_path}')


@click.command()
@click.option("--endpoint", help="endpoint to query (leagues,...)", type=str)
def get_data(endpoint: str):
    endpoints = ('leagues', 'teams')
    apikey = os.environ.get('FOOTBALL_COM_API')
    payload = {}
    headers = {
        'x-rapidapi-key': f'{apikey}',
        'x-rapidapi-host': 'v3.football.api-sports.io'
    }
    if endpoint in endpoints:
        _get_data_from(endpoint=endpoint, headers=headers, payload=payload)
    else:
        logger.info(f'Not implemented yet: "{endpoint}". Choose one of the following: {endpoints}')


if __name__ == '__main__':
    get_data()
