.PHONY: get-league-data
get-league-data:
	poetry run python consumer/api.py --endpoint=${ENDPOINT}

.PHONY: test-consumer
test-consumer:
	poetry run python consumer/test.py --endpoint=${ENDPOINT}