from util.common import check_file_exists_in, open_json
import click as click


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

def clean_elem(elem, k, v):
    out = {}
    if k == 'league':
        out['id'] = elem[k]['id']
        out['name'] = elem[k]['name']
    if k == 'seasons':
        out['seasons'] = clean_seasons(v)
    return out


def clean_seasons(list_of_seasons):
    return [elem['year'] for elem in list_of_seasons]


def filter_dict(list_of_dicts: list[dict], filter_items: tuple) -> list[dict]:
    """
    Pass a list of dicts
    :param list_of_dicts:
    :param filter_items: Tuple of key, eg ('id', 'foobar')
    :return: list of dicts reduced to filter items
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


def filter_seasons_per_leagues(ids: [] = None) -> [{}]:
    """
    praram: ids list of int
    return: list of dicts eg
        [
            {'id': 4, 'name': 'Euro Championship', 'seasons': [2008, 2012, 2016, 2020]},
            {'id': 21, 'name': 'Confederations Cup', 'seasons': [2009, 2013, 2017]},
            {'id': 61, 'name': 'Ligue 1', 'seasons': [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021]}
        ]
    """
    endpoint = 'all_leagues'
    storage_path = f"data/raw_{endpoint}.json"
    # todo: feels wrong and too complex
    # look for map functions here

    filtered = filter_dict(open_json(storage_path)["response"], ('league', 'seasons'))
    prepared = []

    # todo: feels wrong and too complex
    # look for map functions here
    # add id filter
    for item in filtered:
        for k, v in item.items():
            prepared.append(clean_elem(item, k, v))
    print(prepared)
    return prepared


if __name__ == '__main__':
    filter_seasons_per_leagues()
