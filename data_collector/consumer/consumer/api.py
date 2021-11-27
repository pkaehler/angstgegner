import os
import json
import requests
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

apikey = os.environ.get('FOOTBALL_COM_API')
logger.info(apikey)
endpoint = f"leagues"
filters = f"?"

url = f"https://v3.football.api-sports.io/{endpoint}"

payload = {}
headers = {
    'x-rapidapi-key': f'{apikey}',
    'x-rapidapi-host': 'v3.football.api-sports.io'
}

logger.info(f'send request to {url}')
response = requests.request("GET", url, headers=headers, data=payload)

logger.info(response.text)
debug_leagues_format = json.loads(response.text)

with open('../data/leagues.json', 'w', encoding='utf-8') as f:
    json.dump(debug_leagues_format, f)
