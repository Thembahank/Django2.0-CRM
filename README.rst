Django-CRM
==========

Django CRM is opensourse CRM developed on django framework.

Docs at http://django-crm.readthedocs.io for latest documentation

Forked for Docker development and heroku from https://github.com/MicroPyramid/Django-CRM

This project contains the following modules.

   * Contacts
   * Accounts
   * Cases
   * Leads
   * Opportunity
   * Planner

Django 2.07 and Bootstrap 4

Installation - Requirements
===========================



Development locally without docker
===========================


git clone

###Inside your virtual environment run:###

pip install pipenv
pipenv install -r requirements.txt

python manage.py collectstatic --noinput
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0.0.0.0:8000


Development on docker
===========================

Install docker and start a machine
cd into the Django-CRM folder with the Dockerfile
docker build -t djangocrm:v1
docker-compose up

Any issues

DOCKER_OPTS="--dns 8.8.8.8"
docker-machine restart


Deploy to Heroku
===========================

Deploying to Heroku requires that you have both Git and the Heroku CLI installed.
You will also need a Heroku account

1. Install Heroku CLI and Git
Git - https://git-scm.com/book/en/v2/Getting-Started-Installing-Git && https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup
Heroku CLI - https://devcenter.heroku.com/articles/getting-started-with-python#set-up
Sign up - https://signup.heroku.com/dc


2. If you have not already done so, clone the application and cd into the project folder folder
git clone ""


3. Login in to your Heroku account with
$ heroku login
Enter your Heroku credentials
Email: user@example.com
Password:

4. Create an app on Heroku, which prepares Heroku to receive your source code:
$ heroku create










Potential issues on docker

https://docs.docker.com/compose/startup-order/


Test
===========================
  - python manage.py test
  - coverage run --source=accounts,common manage.py test accounts common
  - coverage xml
  - pytest
  - python-codacy-coverage -r coverage.xml




docker-machine create --driver virtualbox myvm1 # Create a VM (Mac, Win7, Linux)
docker-machine create -d hyperv --hyperv-virtual-switch "myswitch" myvm1 # Win10
eval("C:\Program Files\Docker\Docker\Resources\bin\docker-machine.exe" env myvm1)
https://github.com/moby/moby/issues/26330