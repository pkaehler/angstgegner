.PHONY: get-league-data
get-league-data:
	poetry run python consumer/api.py --endpoint=all_leagues

.PHONY: get-teams-per-season-data
get-teams-per-season-data:
	poetry run python consumer/api.py --endpoint=teams_per_season

.PHONY: test-consumer
test-consumer:
	poetry run python consumer/test.py --endpoint=${ENDPOINT}