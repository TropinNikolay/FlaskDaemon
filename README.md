Description
------------
```
"Хранилище файлов с доступом по http"

Реализовать демон, который предоставит HTTP API для загрузки (upload) ,
скачивания (download) и удаления файлов.

Upload:
- получив файл от клиента, демон возвращает в отдельном поле http
response хэш загруженного файла
- демон сохраняет файл на диск в следующую структуру каталогов:
   store/ab/abcdef12345...
где "abcdef12345..." - имя файла, совпадающее с его хэшем.
/ab/ - подкаталог, состоящий из первых двух символов хэша файла.
Алгоритм хэширования - на ваш выбор.

Download:
Запрос на скачивание: клиент передаёт параметр - хэш файла. Демон ищет
файл в локальном хранилище и отдаёт его, если находит.

Delete:
Запрос на удаление: клиент передаёт параметр - хэш файла. Демон ищет
файл в локальном хранилище и удаляет его, если находит.
```

Getting Started
------------

1. `git clone https://github.com/TropinNikolay/FlaskDaemon.git`
2. `cd FlaskDaemon`
3. `virtualenv -p python3 envname`
4. `source envname/bin/activate`
5. `pip install -r requirements.txt`
6. Configure supervisord in `/etc/supervisor`, add this to `supervisord.conf`(don't forget to change paths and username):
```
[program:flaskProject]
command=/home/nikolay/FlaskDaemon/envname/bin/gunicorn -b 127.0.0.1:5000 wsgi:app
directory=/home/nikolay/FlaskDaemon
user=nikolay
autostart=true
autorestart=true
stopasgroup=true
killasgroup=true

[supervisorctl]

[supervisord]
```
7. `sudo service supervisor start`

Now you can go to http://127.0.0.1:5000 in your browser to check it manually.

Running the tests
------------
You can also run tests for this project from **tests/tests.py** module.

Contacts
--------
tropinnikolay@gmail.com