.PHONY: get-league-data
get-league-data:
	poetry run python consumer/api.py get-data --endpoint=all_leagues

.PHONY: get-teams-per-season-data
get-teams-per-season-data:
	poetry run python consumer/api.py get-data --endpoint=teams_per_season


LEAGUE_ID=78
SEASON=2021
.PHONY: get-teams-per-season-data
get-teams-per-season-data:
	poetry run python consumer/api.py get-data --endpoint=teams_per_season --league=${LEAGUE_ID} --season=${SEASON}

.PHONY: filter-seasons-for-all-leagues
filter-seasons-for-all-leagues:
	poetry run python consumer/api.py filter-seasons-per-leagues

.PHONY: filter-seasons-for-leagues
filter-seasons-for-leagues:
	poetry run python consumer/api.py filter-seasons-per-leagues --ids=${IDS}

.PHONY: test-consumer
test-consumer:
	poetry run python consumer/test.py --endpoint=${ENDPOINT}