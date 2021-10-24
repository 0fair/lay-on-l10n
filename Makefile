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

cr_login:
	echo ${YC_CONTAINER_REGISTRY_TOKEN} | docker login \
         --username oauth \
         --password-stdin \
	cr.yandex

build_and_push:
	
