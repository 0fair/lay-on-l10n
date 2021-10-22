.DEFAULT_GOAL=db
.PHONY: test

init_project:
	docker network create moslib-recsys

# Запуск базы данных PostgreSQL
db:
	docker-compose -f build/docker-compose-pg.yml up -d

# Остановка базы данных
stop_db:
	docker-compose -f build/docker-compose-pg.yml stop
