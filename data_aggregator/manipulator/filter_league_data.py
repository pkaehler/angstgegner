from util.common import check_file_exists_in

input_file_name = 'raw_league.json'
output_file = 'league.json'
path = '../data/'


def filter_dict():
    pass


if check_file_exists_in(file_path=path + input_file_name):
    filter_dict(path + input_file_name)

