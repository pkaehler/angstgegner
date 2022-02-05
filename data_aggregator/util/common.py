import os

def check_file_exists_in(file_path: str) -> bool:
    return os.path.exists(file_path)
