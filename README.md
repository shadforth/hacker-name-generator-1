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
# Flask
pip install flask

# Gunicorn
pip install gunicorn
````

## Deployment
````
# Run the program.
python main.py

# Deploy the flask application locally with Bash.
$ export FLASK_APP=app
$ flask run

# Deploy the flask application locally with CMD.
> set FLASK_APP=app
> flask run

# Start command when hosted by third-party.
gunicorn app:app
````
Alternatively, run the program in your favourite IDE that supports Python.

Refer to the Flask documentation for more information: https://flask.palletsprojects.com/en/2.1.x/quickstart/
