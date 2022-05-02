# Hacker Name Generator
Generate a cool hacker name to show off.

## Table of Contents
* [Getting Started](#getting-started)
* [Prerequisites](#prerequisites)
* [Modules](#modules)
* [Running the Application Locally](#running-the-application-locally)
* [Deployment](#deployment)

## Getting Started
Refer to the Flask documentation for more information on how to run or host a Flask application: https://flask.palletsprojects.com/en/2.1.x/quickstart/

### Prerequisites
* [Python](https://www.python.org/downloads/)

### Modules
````
# Flask
pip install flask

# Gunicorn
pip install gunicorn
````

### Running the Application Locally
````
# Run the program.
python main.py

# Deploy the flask application locally with Bash.
$ export FLASK_APP=app
$ flask run

# Deploy the flask application locally with CMD.
> set FLASK_APP=app
> flask run
````

## Deployment
````
# Start command when hosted by third-party.
gunicorn app:app
````
