import json
import os
import logging
import sys

import requests

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def exit_with(message):
    logger.error(f"hard fail due to: --- {message} ---")
    sys.exit()


def check_file_exists_in(file_path: str) -> bool:
    return os.path.exists(file_path)


def save_json(file_path: str, file) -> bool:
    try:
        logger.debug(f'file exists in {file_path}: {os.path.exists(file_path)}')

        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(file, f)
        return True
    except Exception as e:
        logger.warning(f'Could not save file due to: {e}')
        return False


def open_json(file_path: str) -> dict:
    try:
        logger.debug(f'file exists in {file_path}: {os.path.exists(file_path)}')
        with open(file_path, 'r') as file:
            json_dict = json.load(file)
        return json_dict
    except Exception as e:
        logger.error(f'Could not open file due to: {e}')
        return {}


def apply_kwargs(**kwargs) -> str:
    return "&".join(f'{k}={v}' for k, v in kwargs.items())


def has_healthy_status(response) -> bool:
    healthy_status = response.status_code == 200
    text = json.loads(response.text)
    # Football API returns errors or error...
    # 1. "errors": []
    # 2. 'errors': {'required': 'At least one parameter is required.'},
    # 3. {"api": {"error": "[5gNl] The...",...}}
    errors = text.get('errors', [])
    error = text.get('api', {}).get('error', "") # no results
    # TODO: no results {"get": "teams", "parameters": {"league": "78", "season": "2023"}, "errors": [], "results": 0, "paging": {"current": 1, "total": 1}, "response": []}
    has_error = True if errors or error else False
    healthy = True if healthy_status and not has_error else exit_with(errors if errors else error)
    return healthy


def download_data(url, headers, payload):
    logger.info(f'send request to {url}')
    response = requests.request("GET", url, headers=headers, data=payload)
    if has_healthy_status(response):
        raw_data = json.loads(response.text)
        return raw_data
