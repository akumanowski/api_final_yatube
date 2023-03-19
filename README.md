## YATUBE_API
### Описание:

Это учебный проект, в котором отрабатываются навыки разработки API для собственного 
проекта с архитектурой REST, REpresentational State Transfer. 
REST API мы создаем для Django-проекта используя библиотеку Django REST Framework, 
которая ускоряет и упрощает разработку REST API.

Django REST Framework (DRF) предоставляет разработчику весь необходимый 
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
