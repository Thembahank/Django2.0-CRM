#Django-CRM#

Django CRM is opensourse CRM developed on django framework.

Docs at http://django-crm.readthedocs.io for latest documentation

Forked from[Micropyramid](https://github.com/MicroPyramid/Django-CRM) changes include:
 Docker for local development
 Deployment to heroku
 Django compress and sass not used

##Tech stack##
Django 2.0 and Bootstrap 4

##Development locally without docker##
git clone https://yourname@bitbucket.org/digibri/crm.git

######Inside your virtual environment run:######
    pip install pipenv
    pipenv install -r requirements.txt
    python manage.py collectstatic --noinput
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver 0.0.0.0:8000

##Deploy to Heroku##

Deploying to Heroku requires that you have both Git and the Heroku CLI installed.
You will also need a Heroku account

1. Install Heroku CLI and Git
Git - [link](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git && https://git-scm.com/book/en/v2/Getting-Started-First-Time-Git-Setup)
Heroku CLI - [link](https://devcenter.heroku.com/articles/getting-started-with-python)
Sign up - [link](https://signup.heroku.com/dc)


2. If you have not already done so, clone the application and cd into the project folder folder
    git clone ""

3. Login in to your Heroku account with
    $ heroku login
    Enter your Heroku credentials
    Email: user@example.com
    Password:

4. Create an app on Heroku, which prepares Heroku to receive your source code:
    $ heroku create
    $ git push heroku master

5.Run the app locally using heroku
    $ python manage.py collectstatic
    $ heroku local web -f Procfile.windows
    $ heroku local web

6. Make changes and update heroku
if you are installing new packages use pipenv to install so that your pipfile.lock is updated
git add .
git commit -m "Changes to xx"
git push heroku master


##Development on docker##

1. Install docker and start a machine - [link](https://docs.docker.com/install/)

2. cd into the project folder with the Dockerfile

3. Modify database configuration in settings.py
    'HOST':'127.0.0.1' to   'HOST':'db'
If postgres cannot resolve hostname 'db' then use 'HOST':'{insert-your-docker-machine-ip}'
You can run $ docker-machine ip in your terminal to check machine ip

4. Build the image and start containers
    $ docker build -t djangocrm:v1
    $ docker-compose up

That's it. Project should be running at localhost:8000 or {insert-your-docker-machine-ip}:8000

######Potential issues on docker######

DNS misconfiguration issues with pip on docker referred to [here](https://docs.docker.com/get-started/part2/#build-the-app). Run the following to fix:
    $ DOCKER_OPTS="--dns 8.8.8.8"
    $ docker-machine restart
