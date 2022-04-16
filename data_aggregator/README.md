## How to start
1) Sign up for:
https://www.api-football.com/documentation-v3#section/
2) Add `FOOTBALL_COM_API=<your_api_key>` as an environment variable
3) Have fun! Check `Makefile` or section below for available data collection and entrypoints.<br>
   Run `make get-league-data ENDPOINT=league` and check the data folder.
   (data folder is in gitnore, so if it is not created, feel free to do so)

## Structure
Content-root:
* data_aggregator
  * consumer
    * get-teams-per-season-data
    * get-league-data
  * manipulator
    * cleaning and filtering of data

This will be the source for all data handling, eg calling file_exists("data/foobar.json") would check if `.../data_aggregator/data/foobar.json` is existent.

## Implemented:
* All Leagues: `make get-league-data ENDPOINT=all_leagues`
   * Leagues Info
   * Country Info
   * Season Info: Year and coverage
* Teams per season: `make get-teams-per-season-data`
   * Team Info
   * Venue Info

## Open endpoints:
Check https://www.api-football.com/documentation-v3#section/Authentication/API-SPORTS-Account
* Seasons