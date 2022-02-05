import os

def check_file_exists_in(file_path: str) -> bool:
    path = os.path.realpath(__file__)
    data_aggregator_root = os.path.join(path, os.pardir, os.pardir)
    # data_aggregator_root = os.path.dirname(path)
    print(data_aggregator_root)
    print(f'file exists in {file_path}: {os.path.exists(file_path)}')
    return True
