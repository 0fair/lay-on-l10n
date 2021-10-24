.DEFAULT_GOAL=start

# Инициализация проекта. Включает в себя создание отдельной docker network 
init:
	docker network create moslib-recsys

	cp .env .env.dev
	docker-compose build

# Старт проекта для локального тестирования.
# База данных поднимается заранее и c некоторым delay
start:
	docker-compose up moslib-db
	sleep 150
	docker-compose up

# Развертка окружения для разработки
dev:
    docker-compose up moslib-db
	sleep 300
	docker-compose -f ./backend/.dev/docker-compose.yml up --build -d
	docker-compose -f ./frontend/.dev/docker-compose.yml up --build -d

# Очистка файлов проекта (файлы баз данных и кэшей). Запускать с SUDO, если docker запущен из под root
clean:
	rm -r .storage

# Полная сборка решения для проверки работоспособности полной сборки для поставки в облако
build:
	docker-compose build

# Остановка проекта
stop:
	docker-compose stop

# Собрать и запушить проект в Container Registry в Yandex.Cloud. Для этого нужны токены и ID зарегистрированного Registry
build_and_push:
    docker-compose build

	echo ${YC_CONTAINER_REGISTRY_TOKEN} | docker login \
         --username oauth \
         --password-stdin \
	cr.yandex

	docker push "cr.yandex/${YC_CONTAINER_REGISTRY_ID}/moslib-frontend:latest"
	docker push "cr.yandex/${YC_CONTAINER_REGISTRY_ID}/moslib-frontend:latest"
