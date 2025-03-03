from flask import Blueprint

# Create a blueprint for the routes
attendance_bp = Blueprint('attendance', __name__)

# Import routes
from . import attendance_routes

# Register the blueprint in the main application file
# This will be done in app/main.py where the blueprint will be registered with the app instance.