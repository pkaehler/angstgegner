import logging

import click as click
from consumer.api import teams_per_season_endpoint
from manipulator.filter_league_data import filter_dict, clean_seasons
from util.common import open_json

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def clean_leagues(leaguedata):
    keep_leagues = [78] # 78 Bundesliga
    for item in leaguedata:
        if item["league"]["id"] in keep_leagues:
            print(item["leagues"]["name"])
            for season in item["leagues"]["seasons"]:
                year = season["year"]
                print(f'{year}')
        return None


@click.command()
@click.option("--endpoint", help="endpoint to query (leagues,...)", type=str)
def only_for_testing(endpoint: str):
    mapper = {
        "": "",
        "teams": "teams" + teams_per_season_endpoint(),
    }
    logger.debug(f'DEBUG: testing entrypoint')
    storage_path = f"data/raw_{endpoint}{mapper}.json"
    filtered = filter_dict(open_json(storage_path)["response"], ('league', 'seasons'))
    prepared = []
    # season and leagues id from raw leagues

    for item in filtered:
        out = {}
        for k, v in item.items():
            if k == 'league':
                out['id'] = item[k]['id']
                out['name'] = item[k]['name']
            if k == 'seasons':
                out['seasons'] = clean_seasons(v)
        prepared.append(out)


if __name__ == '__main__':
    only_for_testing()
