## YATUBE_API
### Описание:

Это учебный проект, в котором отрабатываются навыки разработки API для собственного проекта с архитектурой 
[REST, REpresentational State Transfer](https://www.ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm). 
REST API мы создаем для Django-проекта используя библиотеку Django REST Framework, 
которая ускоряет и упрощает разработку.

[Django REST Framework (DRF)](https://www.django-rest-framework.org/) предоставляет разработчику весь необходимый 
набор инструментов для создания REST-сервисов на основе Django. 
DRF — это коллекция предустановленных классов, которые предоставляют разработчику инструменты для 
решения штатных задач, возникающих при создании REST API. 

На основе DRF можно минимальным количеством кода преобразовать любое Django-приложение в REST API.

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/akumanowski/api_final_yatube.git
```

```
cd yatube_api
```

Cоздать и активировать виртуальное окружение:

```
python -m venv env
```

```
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```
### Документация к API
Документация разработана с применением стандарта [OpenAPI](https://www.openapis.org/). Этот стандарт 
предназначен для документации REST API-сервисов, независимо от того, на каком языке 
программирования они написаны. OpenAPI описывает, как должен выглядеть файл с документацией.

Существуют различные реализации этого стандарта, но в нашем проекте используется [ReDoc](https://redocly.com/docs/).
После установки и запуска локальной версии проекта, документация для API Yatube доступна по адресу:
```
http://127.0.0.1:8000/redoc/
```