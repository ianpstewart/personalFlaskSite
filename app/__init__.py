#__init__ executes whenever you import a package

from flask import Flask
from config import Config


app = Flask(__name__)
app.config.from_object(Config)


#this is always at the bottom to avoid circular imports
#routes must import app variable so this avoids reciprocal imports
from app import routes
