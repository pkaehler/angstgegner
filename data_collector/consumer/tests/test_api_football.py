import json
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def read_json(path: str) -> dict:
    with open(path) as f:
        jsondict = json.load(f)
        logger.debug(jsondict)
        logger.debug(type(jsondict))
    return jsondict


def get_league_data(data: dict):
    # structure
    # response -> {league,country,seasons}}

    include_countries = ['Germany', 'England']

    countries = [(x['country']['name'], x['league']['name'])
                    for x in data['response'] if x['country']['name'] in include_countries]
    countries2 = [(x['country']['name'], x['league']['name'])
                  for x in data['response'] if x['country']['code']]
    print(countries)
    print(countries2)


def test_league_data_was_read():
    assert True


if __name__ == "__main__":
    path = '../data/leagues.json'
    get_league_data(read_json(path))
