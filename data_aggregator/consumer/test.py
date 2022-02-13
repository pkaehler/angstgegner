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


if __name__ == '__main__':
    only_for_testing()
