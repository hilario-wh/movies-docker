# Usa la imagen base de Python
FROM python:3.9

# Configura las variables de entorno de Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Establece el directorio de trabajo en /app
WORKDIR /app

# Instala las dependencias del sistema requeridas para Supervisor
RUN apt-get update && apt-get install -y supervisor

# Copia los archivos de requerimientos de Django a la imagen y luego instala las dependencias
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copia los archivos de la aplicación Django a la imagen
COPY . /app/

# Configura Supervisor
RUN cp /app/deploy/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Expone el puerto 8000 (o el puerto que uses para ejecutar Django)
EXPOSE 8000

# Ejecuta Supervisor como proceso principal en el contenedor
CMD ["supervisord", "-n"]