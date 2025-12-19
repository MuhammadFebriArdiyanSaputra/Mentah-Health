# Mental Health App

A simple Flask web application for mental health support.

## Setup

1. Install Python 3.10 or higher.
2. Install virtualenv: `pip install virtualenv`
3. Create a virtual environment: `virtualenv env`
4. Activate the environment: `env\Scripts\activate` (Windows)
5. Install dependencies: `pip install -r requirements.txt`
6. Run the app: `python app.py`

## Docker

1. Build the image: `docker build -t mental-health-app .`
2. Run the container: `docker run -p 5000:5000 mental-health-app`

## Deployment

This app can be deployed to Heroku or other platforms using the Procfile.
