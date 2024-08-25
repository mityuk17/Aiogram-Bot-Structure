build_develop:
	docker compose -f docker-compose.develop.yaml build
run_develop:
	docker compose -f docker-compose.develop.yaml up
build_and_run_develop:
	docker compose -f docker-compose.develop.yaml up --build


build_prod:
	docker compose -f docker-compose.prod.yaml build
run_prod:
	docker compose -f docker-compose.prod.yaml up -d
build_and_run_prod:
	docker compose -f docker-compose.prod.yaml up --build -d

