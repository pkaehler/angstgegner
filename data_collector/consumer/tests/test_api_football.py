import json
import logging
import pytest

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# arrange
@pytest.fixture()
def input_data() -> dict:
    # think about better solution for path
    # this path only works if pytest is executed one level above
    path = 'tests/data/world_france_germany.json'
    with open(path, 'r') as f:
        jsondict = json.load(f)
    return jsondict

#execute
def get_league_data(data: dict) -> dict:
    # structure
    # response -> [{league,country,seasons}}]

    include_countries = ['Germany', 'England']

    countries = [{(x['country']['name'], x['league']['name']): x['seasons']}
                 for x in data['response'] if x['country']['name'] in include_countries]
    countries2 = [{(x['country']['name'], x['league']['name']): x['seasons']}
                  for x in data['response'] if x['country']['code']]
    logger.info(countries)
    return countries

#assert
def test_league_data_was_read(input_data):
    assert bool(get_league_data(input_data))
