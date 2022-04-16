import os
import json

import click as click
import requests
import logging

from util.common import check_file_exists_in, save_json, open_json
from manipulator.filter_league_data import filter_dict, clean_seasons

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def download_data(url, headers, payload):
    logger.info(f'send request to {url}')
    response = requests.request("GET", url, headers=headers, data=payload)
    raw_data = json.loads(response.text)
    return raw_data


def teams_per_season_endpoint(league: int, season: int) -> str:
    """
    returns query params
    """
    # https://v3.football.api-sports.io/teams?league=78&season=2021
    return f"?league={league}8&season={season}"


mapper = {
    "": "",
    "teams_per_season": "teams" + teams_per_season_endpoint(78, 2021),
    "all_leagues": "leagues",
}


def _get_data_from(endpoint: str, headers: dict, payload: dict, *kwargs):
    endpoint = f"{endpoint}"
    if args:
        for arg in args:
            print(f'passed arg: {arg}')
    url = f"https://v3.football.api-sports.io/{mapper[endpoint]}"
    storage_path = f"data/raw_{endpoint}.json"
    logger.info(f'Try fetching data from {url}')
    if check_file_exists_in(storage_path):
        logger.info(f'Stopped. File {storage_path} already exists.')
    else:
        data = download_data(url=url, headers=headers, payload=payload)
        if save_json(file_path=storage_path, file=data):
            logger.info(f'File saved to {storage_path}')


@click.group("cli")
@click.pass_context
def cli(ctx):
    """
    Helper if context is needed
    """
    ctx.obj = "some context here"


@cli.command("get-data")
@click.pass_context
@click.option("--endpoint", help="endpoint to query (leagues,...)", type=str)
def get_data(ctx, endpoint: str, league_id: int = None, season: int = None):
    endpoints = ('all_leagues', 'teams_per_season')
    apikey = os.environ.get('FOOTBALL_COM_API')
    payload = {}
    headers = {
        'x-rapidapi-key': f'{apikey}',
        'x-rapidapi-host': 'v3.football.api-sports.io'
    }
    if endpoint in endpoints:
        if league_id and season:
            _get_data_from(endpoint=endpoint, headers=headers, payload=payload, league_id=league_id, season=season)
        else:
            _get_data_from(endpoint=endpoint, headers=headers, payload=payload)
    else:
        logger.info(f'Not implemented yet: "{endpoint}". Choose one of the following: {endpoints}')


@cli.command("filter-seasons-per-leagues")
@click.pass_context
@click.option("--ids", help="clean list of season(years) for a leagues or all leagues", required=False)
def filter_seasons_per_leagues(ctx, ids: list()) -> dict:
    """
    praram: ids list of int
    return: list of dicts eg 
        [
            {'id': 4, 'name': 'Euro Championship', 'seasons': [2008, 2012, 2016, 2020]}, 
            {'id': 21, 'name': 'Confederations Cup', 'seasons': [2009, 2013, 2017]}, 
            {'id': 61, 'name': 'Ligue 1', 'seasons': [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]}
        ]
    """
    endpoint = 'all_leagues'
    storage_path = f"data/raw_{endpoint}.json"
    filtered = filter_dict(open_json(storage_path)["response"], ('league', 'seasons'))
    prepared = []

    for item in filtered:
        out = {}
        for k, v in item.items():
            if k == 'league':
                out['id'] = item[k]['id']
                out['name'] = item[k]['name']
            if k == 'seasons':
                out['seasons'] = clean_seasons(v)
        prepared.append(out)
    if ids:
        return {k: v for k, v in prepared.items() if k in ids}
    else:
        return prepared


if __name__ == '__main__':
    cli()
