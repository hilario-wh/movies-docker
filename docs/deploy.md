## Comandos utilizados para crear el proyecto
- Instalar Django
```
pip install django
```
- Crear proyecto en django
```
pip install django
```
- Crear una nueva aplicacion
```
python manage.py startapp movies
```

## Correr el proyecto en local
- Crear entorno
```
mkvirtualenv practicas-deploy
```

- Instalar requerimientos
```
pip install -r requirements.txt
```

- Ejecutar migraciones
```
python manage.py makemigrations
python manage.py migrate
```

- Crear superusuario
```
python manage.py createsuperuser
```

- Ejecutar aplicacion
```
python manage.py runserver
```

## Deploy

### Instalar uWSGI
```
pip install uwsgi
```

### Configurar uWSGI
Una vez instalado uWSGI, debemos configurarlo para que sirva nuestra aplicación de Django. En la raíz de tu proyecto de Django, crea un archivo llamado uwsgi.ini con el siguiente contenido:
```
[uwsgi]
chdir=/home/{host_user}/Documentos/github/practicas-deploy
module=practicas-deploy.wsgi:application
env=DJANGO_SETTINGS_MODULE=practicas_deploy.settings
master=true
pidfile=/tmp/practicas_deploy.pid
socket=/tmp/practicas_deploy.sock
vacuum=true
max-requests=5000
harakiri=30
```

### Configurar NGINX
Ahora que hemos configurado uWSGI, debemos configurar Nginx para actuar como un servidor proxy para nuestras solicitudes web. En la terminal de tu servidor, instala Nginx con el siguiente comando:
```
sudo apt-get update
sudo apt-get install nginx
```

Una vez que Nginx esté instalado, debemos configurarlo. En el archivo /etc/nginx/sites-available/tu_proyecto (donde tu_proyecto es el nombre de tu proyecto de Django), escribe el siguiente contenido:
```
server {
    listen 80;
    server_name practicas-deploy.com;

    location / {
        include uwsgi_params;
        uwsgi_pass unix:/tmp/practicas-deploy.sock;
    }
}

```

```
```