#!/bin/bash

NAME="siv" # Nombre de la aplicación
DJANGODIR=/home/siv_project/siv/siv # Ruta de la carpeta donde esta la aplicación reemplazar <user> con el nombre de usuario
SOCKFILE=/home/siv_project/siv/run/gunicorn.sock # Ruta donde se creará el archivo de socket unix para comunicarnos
USER=jairotft # Usuario con el que vamos a correr la app
GROUP=jairotft # Grupo con el que se va a correr la app
NUM_WORKERS=3 # Número de workers que se van a utilizar para correr la aplicación
DJANGO_SETTINGS_MODULE=/home/siv_project/siv/siv/siv # ruta de los settings
DJANGO_WSGI_MODULE=siv.wsgi # Nombre del módulo wsgi

echo "Starting $NAME as `whoami`"

# Activar el entorno virtual
cd $DJANGODIR
workon miapp 
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

# Crear la carpeta run si no existe para guardar el socket linux
RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

# Iniciar la aplicación django por medio de gunicorn
exec ../bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user=$USER --group=$GROUP \
  --bind=unix:$SOCKFILE \
  --log-level=debug \
  --log-file=-