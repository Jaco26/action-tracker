import os
from flask import Flask, jsonify, abort
from datetime import datetime

# my utilities
from .util.custom_api_response import ApiFlask
from .util.json_encoder import CustomJSONEncoder
from .util.custom_error_handler import custom_error_handler
from .util import jwt

# database threaded connection pool
from .db import pool

# some sql scripts to create tables and insert initial values
from . import queries

# blueprints
from .blueprints.v1.auth import auth_bp_v1
from .blueprints.v1.action_category import action_category_bp_v1

def create_app():
  app = ApiFlask(__name__)
  app.json_encoder = CustomJSONEncoder

  app.config['JWT_SECRET_KEY'] = os.environ['JWT_SECRET_KEY']
  app.config['JWT_BLACKLIST_ENABLED'] = True

  pool.init_app(app)
  custom_error_handler.init_app(app)
  jwt.init_app(app)

  app.register_blueprint(auth_bp_v1, url_prefix="/api/v1/auth")
  app.register_blueprint(action_category_bp_v1, url_prefix="/api/v1/action-category")

  # @app.before_first_request
  # def do_before():
  #   queries.drop_tables()
  #   queries.create_tables()
  #   # queries.insert_user_and_action_category()
  #   # queries.insert_test_values()

  @app.route("/")
  def index():
    return jsonify(message="Hello You!", date=datetime.now())

  return app