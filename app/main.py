from flask import Flask, jsonify, abort
from datetime import datetime

from .util.json_encoder import CustomJSONEncoder
from .util.custom_error_handler import custom_error_handler
from .db import pool

from . import queries

from .blueprints.v1.auth import auth_bp_v1

def create_app():
  app = Flask(__name__)
  app.json_encoder = CustomJSONEncoder

  pool.init_app(app)
  custom_error_handler.init_app(app)

  app.register_blueprint(auth_bp_v1, url_prefix="/api/v1/auth")

  # @app.before_first_request
  # def do_before():
  #   queries.drop_tables()
  #   queries.create_tables()
  #   queries.insert_user_and_action_category()
  #   queries.insert_test_values()

  @app.route("/")
  def index():
    return jsonify(message="Hello You!", date=datetime.now())

  return app