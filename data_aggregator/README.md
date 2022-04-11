## How to start
1) Sign up for:
https://www.api-football.com/documentation-v3#section/
2) Add `FOOTBALL_COM_API=<your_api_key>` as an environment variable
3) Have fun eg run `make get-league-data ENDPOINT=league` and check the data folder.
   (data folder is in gitnore, so if it is not created, feel free to do so)

## Structure
Content-root:
* data_aggregator

This will be the source for all data handling, eg calling file_exists("data/foobar.json") would check if `.../data_aggregator/data/foobar.json` is existent.

## Implemented:
* Leagues:
   * Leagues Info
   * Country Info
   * Season Info: Year and coverage
* Teams:
   * Team Info
   * Venue Info
* 

* Season

## Open endpoints:
Check https://www.api-football.com/documentation-v3#section/Authentication/API-SPORTS-Account
* Seasons