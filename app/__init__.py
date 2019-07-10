#__init__ executes whenever you import a package

from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Config)
database = SQLAlchemy(app)

#this is always at the bottom to avoid circular imports
#routes must import app variable so this avoids reciprocal imports
from app import routes, models
