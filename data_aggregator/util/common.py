import json
import os
import logging
import requests

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


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


def _apply_kwargs(**kwargs) -> str:
    return "&".join(f'{k}={v}' for k, v in kwargs.items())


def download_data(url, headers, payload):
    logger.info(f'send request to {url}')
    response = requests.request("GET", url, headers=headers, data=payload)
    raw_data = json.loads(response.text)
    return raw_data
