import json
import os
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def check_file_exists_in(file_path: str) -> bool:
    path = os.path.realpath(__file__)
    os.path.join(path, os.pardir, os.pardir)
    logger.debug(f'file exists in {file_path}: {os.path.exists(file_path)}')
    return os.path.exists(file_path)


def save_json(file_path: str, file) -> bool:
    try:
        path = os.path.realpath(__file__)
        os.path.join(path, os.pardir, os.pardir)
        logger.debug(f'file exists in {file_path}: {os.path.exists(file_path)}')

        with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(file, f)
        return True
    except Exception as e:
        logger.warning(f'Could not save file due to: {e}')
        return False
