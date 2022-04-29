# Hacker Name Generator
Generate a cool hacker name to show off.

## Table of Contents
* [Getting Started](#getting-started)
* [Prerequisites](#prerequisites)
* [Modules](#modules)
* [Deployment](#deployment)

## Getting Started

### Prerequisites
* Python

### Modules
````
# Flask 2.1.1
pip install flask

# Gunicorn 20.1.0
pip install gunicorn
````

## Deployment
To run the program simply run the code in your favourite IDE that supports Python. Alternatively, you can start the web app through the command line, or via a thirdy-party host.

Refer to the Flask documentation for more information: https://flask.palletsprojects.com/en/2.1.x/quickstart/

````
# Deploy the flask application locally with Bash.
$ export FLASK_APP=app
$ flask run

# Deploy the flask application locally with CMD.
> set FLASK_APP=app
> flask run

# Start command when hosted by by third-party.
gunicorn app:app
````
