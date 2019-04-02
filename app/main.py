import os
from flask import Flask, jsonify, abort, request, render_template
from flask_migrate import Migrate
from datetime import datetime

# my utilities
from .util.custom_api_response import ApiFlask
from .util.json_encoder import CustomJSONEncoder
from .util.custom_error_handler import custom_error_handler
from .util import jwt

# flask_sqlalchemy database
from .fsa_db import db

# database threaded connection pool
from .db import pool

# some sql scripts to create tables
from .queries.v1 import create_tables

# blueprints
from .blueprints.v1.auth import auth_bp_v1
from .blueprints.v1.action_category import action_category_bp_v1
from .blueprints.v1.action_taken import action_taken_bp_v1

def create_app(config=None):
  app = ApiFlask(__name__, static_folder="./templates/static")
  app.json_encoder = CustomJSONEncoder

  if config:
    app.config.from_object(config)

  app.config['JWT_SECRET_KEY'] = os.environ['JWT_SECRET_KEY']
  app.config['JWT_BLACKLIST_ENABLED'] = True
  app.config["SQLALCHEMY_DATABASE_URI"] = 
  
  db.init_app(app)
  pool.init_app(app)
  custom_error_handler.init_app(app)
  jwt.init_app(app)

  migrate = Migrate(app, db)

  app.register_blueprint(auth_bp_v1, url_prefix="/api/v1/auth")
  app.register_blueprint(action_category_bp_v1, url_prefix="/api/v1/action-category")
  app.register_blueprint(action_taken_bp_v1, url_prefix="/api/v1/action-taken")

  @app.route("/", defaults={'path': ''})
  @app.route("/<path:path>")
  def index(path):
    return render_template("index.html")

  return app