import os
import click as click
import logging

from consumer.endpoints import teams_per_season_endpoint
from util.common import check_file_exists_in, save_json, apply_kwargs, download_data

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


mapper = {
    "": "",
    "teams_per_season": {"endpoint": "teams",
                         "query_params": teams_per_season_endpoint,
                         },
    "all_leagues": {"endpoint": "leagues",
                    "query_params": None,
                    },
}


def _get_data_from(endpoint: str, headers: dict, payload: dict, **kwargs):
    endpoint = f"{endpoint}"
    url = f"https://v3.football.api-sports.io/{mapper[endpoint]['endpoint']}"
    if kwargs:
        url = url + '?' + apply_kwargs(**kwargs)
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
@click.option("--league-id", help="pass an id to query only one league", type=int, required=False)
@click.option("--season", help="pass an id to query only one league", type=int, required=False)
def get_data(ctx, endpoint: str, league_id: int = None, season: int = None):
    endpoints = ('all_leagues', 'teams_per_season')
    apikey = os.environ.get('FOOTBALL_COM_API')
    payload = {}
    headers = {
        'x-rapidapi-key': f'{apikey}',
        'x-rapidapi-host': 'v3.football.api-sports.io'
    }

    if endpoint in endpoints:
        # TODO: apply check if kwargs return valid endpoint
        if league_id and season:
            # TODO: kw like league and season has to conform to query params here:
            #  https://www.api-football.com/documentation-v3#operation/get-teams
            #  think about how to be agnostic of API definition or have those in one place to adapt to changes
            _get_data_from(endpoint=endpoint, headers=headers, payload=payload, league=league_id, season=season)
        else:
            _get_data_from(endpoint=endpoint, headers=headers, payload=payload)
    else:
        logger.info(f'Not implemented yet: "{endpoint}". Choose one of the following: {endpoints}')


if __name__ == '__main__':
    cli()
