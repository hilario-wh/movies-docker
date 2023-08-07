## Proyecto de practica Docker
El siguiente proyecto es un crud basico de peliculas montado con docker y las siguientes tecnologias:
 - Django
 - NGINX
 - Postgres
 - Supervisor (No prod)


## Correr el proyecto:
Requerimientos:
- Tener libre el puerto 80
- Tener instalado Docker y con suficientes privilegios para realizar las siguientes acciones

**Alojar el dominio djmovie.com**

Editar el archivo hosts:
```shell
sudo nano /etc/hosts
```
Agregar la siguiente linea al final:
```shell
127.0.0.1       djmovie.com
```

**Ejecutar el contenedor**
```shell
docker compose build
docker compose up
```
