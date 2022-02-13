import logging

import click as click
from manipulator.filter_league_data import filter_dict, clean_seasons
from util.common import open_json

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


@click.command()
@click.option("--endpoint", help="endpoint to query (leagues,...)", type=str)
def only_for_testing(endpoint: str):

    logger.debug(f'DEBUG: testing entrypoint')
    storage_path = f"data/raw_{endpoint}.json"
    filtered = filter_dict(open_json(storage_path)["response"], ('league', 'seasons'))
    for item in filtered:
        for k, v in item.items():

            cleaned = clean_seasons()


if __name__ == '__main__':
    only_for_testing()
