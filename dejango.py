#!/usr/bin/python3
import os
import sys
import subprocess
import logging

# installing the packages required
# logger = logging.getLogger(__name__)
# logger.info('Installing the required packages...')    # need to color the logging here!

os.system('pip install gunicorn psycopg2-binary django-heroku dj-database-url')


# create a requirements.txt file
os.system('pip freeze > requirements.txt')  # display a logging here, let user know if
                                            # the installation is complete

# create a Procfile
project_directory = os.getcwd()
split_dirs = project_directory.split('/')
project_name = split_dirs[-1]

# print(project_name)   # code to check if the project_name is correct

# with open('Procfile', 'x') as f:
#     f.write('web: gunicorn ' +project_name+'.wsgi:application')  # make sure the project name is correct


# print('hello am running')
