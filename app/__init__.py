from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__) # variable as an instance of Flask object - a member of the package and will be by the view functions to define their routes
app.config.from_object(Config)
login = LoginManager(app)
login.login_view='login'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models # this line is simply importing everything from routes.py to make it visible to flask when it is reading the endpoints (the same for the next line)
from app import other_routes
