# Lay-on-L10n
# Рекомендательная система для московских библиотек

Строим рекомендательную систему для хакатона Лидеры цифровой трансформации
# Пререквизиты к установке и настройке:
Большинство команд для развертывания проекта производятся локально из командной строки

0. Установить make
Для Windows:
```bash
choco install make
```
Для Ubuntu
```bash
sudo apt update
sudo apt install make
```
Для MacOS
```bash
sudo xcode-select -switch /Applications/Xcode.app/Contents/Developer
```
1. Поставить docker и docker-compose
    https://docs.docker.com/engine/install/
    https://docs.docker.com/compose/install/

# Установка
0. Инициализировать проект: создать docker network, проставить .env файл и запустить сборку с помощью команды
```bash
make init
```
1. Необходимо запустить проект
```bash
make start
```
2. Зайти по адресу http://localhost

