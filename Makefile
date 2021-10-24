.DEFAULT_GOAL=start

# Инициализация проекта. Включает в себя создание отдельной docker network 
init:
	docker network create moslib-recsys

	cp .env .env.dev
	docker-compose build

# Полная сборка решения для проверки работоспособности полной сборки для поставки в облако
build:
	docker-compose build

# Старт проекта для локального тестирования.
# База данных поднимается заранее и c некоторым delay
start:
	docker-compose up

# Развертка окружения для разработки
dev:
	docker-compose 

# Очистка файлов проекта (файлы баз данных и кэшей). Запускать с SUDO, если docker запущен из под root
clean:
	rm -r .storage

# Остановка проекта
stop:
	docker-compose stop

build_and_push:
    docker-compose build

	echo ${YC_CONTAINER_REGISTRY_TOKEN} | docker login \
         --username oauth \
         --password-stdin \
	cr.yandex

	docker push "cr.yandex/${YC_CONTAINER_REGISTRY_ID}/moslib-frontend:latest"
	docker push "cr.yandex/${YC_CONTAINER_REGISTRY_ID}/moslib-frontend:latest"
