# Usa la imagen base de Nginx
FROM nginx:latest

# Elimina la configuración de Nginx predeterminada
RUN rm /etc/nginx/conf.d/default.conf

# Copia el archivo de configuración personalizado de Nginx al contenedor
COPY ./deploy/nginx.conf /etc/nginx/conf.d/

# Expone el puerto 80 para que el tráfico pueda llegar al proxy
EXPOSE 80

# Inicia Nginx al ejecutar el contenedor
CMD ["nginx", "-g", "daemon off;"]
