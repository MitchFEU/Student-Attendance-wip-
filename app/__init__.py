from flask import Flask

app = Flask(__name__)

from app.routes import *  # Import routes to register them with the app