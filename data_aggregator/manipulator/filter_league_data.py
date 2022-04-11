from util.common import check_file_exists_in, open_json

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


def clean_seasons(list_of_seasons):
    return [elem['year'] for elem in list_of_seasons]


def filter_dict(list_of_dicts: list[dict], filter_items: tuple) -> list[dict]:
    """
    Pass a list of dicts
    :param list_of_dicts:
    :param filter_items: Tuple of key, eg ('id', 'foobar')
    :return: dict
    """
    result = []
    for elem in list_of_dicts:
        result.append({k: v for k, v in elem.items() if k in filter_items})
    return result


def get_all_ids_and_seasons() -> list:
    """

    :return: List of all league ids
    """
    pass
