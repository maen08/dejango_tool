#!/usr/bin/python3
import os
import sys
import subprocess
import logging


# pypi needs this instead of print statements
# change all prints to be logging
# use the colored logging statements


# I:THE DJANGO PART-SETTING UP EVERYTHING

# ask the user to enter the project-name
project_name = input('Whats your project name:')

   
try:
    os.system('pip install gunicorn psycopg2-binary django-heroku dj-database-url')
    print('DONE: All packages are installed successfully')

except FileExistsError:
    print('DONE: All packages are installed successfully')


# create a requirements.txt file
try:
    os.system('pip freeze > requirements.txt')
    print('DONE: requirements.txt file created')

except FileExistsError:
    print('DONE: requirements.txt file created')



# create a Procfile
try:
    with open('Procfile', 'x') as f:
        # make sure the project name is correct
        f.write('web: gunicorn ' + project_name + '.wsgi:application')
    print('DONE: Procfile created')


except FileExistsError:
    print('DONE: Procfile created')


# project_directory = os.getcwd()
# split_dirs = project_directory.split('/')
# project_folder = split_dirs[-1] 



# a function to prepend the import statement
to_settings = os.chdir(project_name)

def line_prepender(filename, line):
    with open(filename, 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(line.rstrip('\r\n') + '\n' + content)

try:
    line_prepender('settings.py', 'import dj_database_url')
    line_prepender('settings.py', 'import django_heroku')

except FileExistsError:
    print('DONE: All packages are imported')



print('Remember to push everything on Github')


# II: HEROKU PART-DEPLOYMENT

try:
    print("INFO: Wait to login to heroku...")
    # os.system('heroku login')
    
except:
    print('INFO: Please login to heroku')

# creating a heroku domain-name
domain_name = input('Choose the domain name: ')
os.system('heroku create' +' '+ domain_name)

# push to heroku
os.system('git push heroku master')
os.system('heroku run python manage.py makemigrations')
os.system('heroku run python manage.py migrate')