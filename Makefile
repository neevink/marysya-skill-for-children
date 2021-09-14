PROJECT_NAME ?= simple-service
VERSION = $(shell python3 setup.py --version | tr '+' '-')

all:
	@echo "clean			- Очистить файлы, созданные distutils"
	@echo "sdist			- Создать исходник"
	@echo "devenv			- Пересоздать переменную окружения и заново установить зависимости"
	@echo "run				- Запустить приложение"
	@exit 0

clean:
	rm -fr *.egg-info dist

sdist: clean
	# официальный способ дистрибуции python-модулей
	python3 skill/setup.py sdist

devenv: clean
	rm -rf venv
	# создаем новое окружение
	python3.9 -m venv venv
	# обновляем pip
	venv/bin/pip install -U pip
	# устанавливаем основные + dev зависимости из extras_require (см. setup.py)
	venv/bin/pip install -Ue '.[dev]'
