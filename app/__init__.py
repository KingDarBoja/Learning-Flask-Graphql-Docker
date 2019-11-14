"""Module to initialize and config our Flask App"""
from flask import Flask

# Initialize a Flask WSGI object
app = Flask(__name__)

# Load default config values based on enviroment
if app.config["ENV"] == "production":
    app.config.from_object("config.DevelopmentConfig")
elif app.config["ENV"] == "testing":
    app.config.from_object("config.TestingConfig")
else:
    app.config.from_object("config.DevelopmentConfig")

# TODO: Provide override of default config with envvar
# app.config.from_envvar("YOUR_APPS_ENVVAR")

# Import our routes definitions
from app import views