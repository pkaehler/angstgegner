from util.common import check_file_exists_in

# todo:
# define schema to keep only this information
# "response": 
#   [
#     {
#       "league": 
#           {
#               "id": int,
#               "name": str,
#                "type": st",
#                "logo": str,
#             },
#             "country": {
#                 "name": str,
#                 "code": null,
#                 "flag": null
#             },
#             "seasons": [
#                 {
#                     "year": int,
#                     "start": str,
#                     "end": str,
#                     "current": bool,
#                     "coverage": {
#                         "fixtures": {
#                             "events": bool,
#                             "lineups": bool,
#                             "statistics_fixtures": bool,
#                             "statistics_players": bool
#                         },
#                         "standings": bool,
#                         "players": bool,
#                         "top_scorers": bool,
#                         "top_assists": bool,
#                         "top_cards": bool,
#                         "injuries": bool,
#                         "predictions": bool,
#                         "odds": bool
#                     }
#                 },
#           
#             ]
#         },

input_file_name = 'raw_league.json'
output_file = 'league.json'
path = '../data/'


def filter_dict(jsondict: dict, filter) -> dict:
    """
    Pass a dict
    :param dict: Json /dict
    :param filter: Tuple of key, eg ('id', 'foobar')
    :return: dict
    """
    return {k: v for k, v in jsondict if k in filter}


if check_file_exists_in(file_path=path + input_file_name):
    filter_dict(path + input_file_name)
