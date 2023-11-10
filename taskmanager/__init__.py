import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Load environment variables from 'env.py' if it exists
if os.path.exists("env.py"):
    import env

# Set Flask configuration variables
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")

# Initialize Flask-SQLAlchemy
db = SQLAlchemy(app)

# Import routes after initializing the app and db
from taskmanager import routes