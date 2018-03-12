#!/bin/bash

cd
sudo su
apt-get update
apt-get upgrade -y

echo "Sistema actualizado"
echo "version de python 2"
python3 -V

echo "Instalando dependencias"
apt-get install build-essential libssl-dev libffi-dev python-dev -y
apt-get install python3-pip -y
apt-get install python-setuptools -y
apt-get build-dep python-psycopg2 -y
apt-get install nginx postgresql postgresql-contrib supervisor -y
apt-get install git -y
apt-get install virtualenv -y
exit

echo "Dependecias instaladas"

echo "Generado ambiente"
pip3 install virtualenvwrapper

echo "export WORKON_HOME=$HOME/.virtualenvs" >> .bashrc
echo "export PROJECT_HOME=$HOME/Devel" >> .bashrc
echo "export VIRTUALENVWRAPPER_SCRIPT=$HOME/.local/bin/virtualenvwrapper.sh" >> .bashrc
echo "source $HOME/.local/bin/virtualenvwrapper_lazy.sh" >> .bashrc

source .bashrc
mkvirtualenv siv_app --python=$(which python3)
workon siv_app

pip install psycopg2
 
echo "Dependencias de ambiente generado" 

echo "Iniciando proyecto"
whoami > session
sudo su
mkdir -p /home/siv_project
export USERSESSION="$(cat session)"
chown $USERSESSION /home/siv_project
exit
cd /home/siv_project

echo "------------------------------"
echo "Clonando proyecto"

git clone https://github.com/Jairo95/siv.git


echo "Proceso finalizado"



