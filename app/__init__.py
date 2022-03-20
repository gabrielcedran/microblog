from flask import Flask
from config import Config

app = Flask(__name__) # variable as an instance of Flask object - a member of the package and will be by the view functions to define their routes
app.config.from_object(Config)

from app import routes # this line is simply importing everything from routes.py to make it visible to flask when it is reading the endpoints (the same for the next line)
from app import other_routes
