build-dev:
	docker compose -f docker-compose.develop.yaml build
run-dev:
	docker compose -f docker-compose.develop.yaml up
build-run-dev:
	docker compose -f docker-compose.develop.yaml up --build

stop-dev:
	docker compose -f docker-compose.prod.yaml stop


build-prod:
	docker compose -f docker-compose.prod.yaml build
run-prod:
	docker compose -f docker-compose.prod.yaml up -d
build-run-prod:
	docker compose -f docker-compose.prod.yaml up --build -d

stop-prod:
	docker compose -f docker-compose.prod.yaml stop
