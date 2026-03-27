up:
	docker compose up -d --build

down:
	docker compose down -v

test:
	docker compose -f docker-compose.yml -f docker-compose.override.yml up --build --abort-on-container-exit --exit-code-from test_runner

logs:
	docker compose logs -f