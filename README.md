### How to run project
1. `git clone https://github.com/TropinNikolay/FlaskDaemon.git`
2. `cd FlaskDaemon`
3. `virtualenv -p python3 envname`
4. `source envname/bin/activate`
5. `pip install -r requirements.txt`
6. Configure supervisord in `/etc/supervisor` (add this to `supervisord.conf`, change paths!):
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