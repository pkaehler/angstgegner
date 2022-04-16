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


@click.option("--ids", help="clean list of season(years) for a leagues or all leagues", required=False)
def filter_seasons_per_leagues(ids: []) -> {[]}:
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
    filtered = filter_dict(open_json(storage_path)["response"], ('league', 'seasons'))
    prepared = []

    for item in filtered:
        out = {}
        for k, v in item.items():
            if k == 'league':
                out['id'] = item[k]['id']
                out['name'] = item[k]['name']
            if k == 'seasons':
                out['seasons'] = clean_seasons(v)
        prepared.append(out)
    if ids:
        print()
        return [{k: v for k, v in prepared.items() if k in ids}]
    else:
        return prepared
