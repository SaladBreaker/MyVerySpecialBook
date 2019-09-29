# My Very Special Book



## Installation

The program is created in a virtual environment using pipenv.



To install pipenv use:

> $ pip3 install pipenv



To install the virtual environment use the following command in the folder with the Pipfile:

> $ pipenv install



## Usage

To run the program execute:

> $ pipenv shell

> $ python main.py

## Content

The project has two important components:

- the flask_site containing the code for the website
- the tests for the site

## Flask_site folder:
This folder is responsible for basically everything and that is why I will dive it in 2:

- The python flask code
- The HTML, CSS, JS part

### Flask code
The flask code  is found in the flask_site folder in every .py file. The current .py files are:

- app.py ( responsible for creating the app and setting important properties for it. Also here the database is loaded)
- forms.py ( here it is found the add book forum, made with wtforms)
- models.py (the database book table model is found here, made with SQLAlchemy, the connection between this and the  PostgreSQL is done in app.py)
- routes.py ( this sets the site routs, loads html and  does the database queries)

### Templates + static
In the templates folder the html files are found
The static folder contains files generated with Bootstrap Studio for the visual part of the site.

## Known problems
- the  dropzone lib is in conflict with the flask form, so if it is used the wtforms can not send POST requests and thus for the moment it is commented in the layout.html file

## Future work
- add more tests for the project
- add a admin account that can delete books from the database
- store the file added in the addfile route
- use a python library similar to dropzone lib to allow the files to be drag and drop on the page

## Heroku link

https://myveryveryspecialbookbot.herokuapp.com/
