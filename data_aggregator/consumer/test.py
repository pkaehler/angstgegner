import click
import pprint
import json
import os
from consumer.api import mapper
import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@click.group("cli")
@click.pass_context
def cli(ctx):
   """An example CLI for interfacing with a document"""
   ctx.obj = "some context here"


@cli.command("get_data")
@click.pass_context
@click.option("--endpoint", help="endpoint to query (leagues,...)", type=str)
def get_data(ctx, endpoint):
    print(endpoint)
#     endpoints = ('all_leagues', 'teams_per_season')
#     apikey = os.environ.get('FOOTBALL_COM_API')
#     payload = {}
#     headers = {
#         'x-rapidapi-key': f'{apikey}',
#         'x-rapidapi-host': 'v3.football.api-sports.io'
#     }
    pprint.pprint(ctx.obj)
#     pprint.pprint(type(ctx.obj))
#     print(endpoint)
#     #if endpoint in endpoints:
#     #    _get_data_from(endpoint=endpoint, headers=headers, payload=payload)
#     #else:
#     #    logger.info(f'Not implemented yet: "{endpoint}". Choose one of the following: {endpoints}')

if __name__ == '__main__':
   cli()