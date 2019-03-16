from flask import Flask, jsonify
from datetime import datetime

from .util.json_encoder import CustomJSONEncoder
from .db import pool
from . import queries

def create_app():
  app = Flask(__name__)
  app.json_encoder = CustomJSONEncoder

  pool.init_app(app)

  # @app.before_first_request
  # def do_before():
  #   queries.drop_tables()
  #   queries.create_tables()
  #   queries.insert_user_and_action_category()
  #   queries.insert_test_values()

  @app.route("/")
  def index():
    return jsonify(message="Hello You!", date=datetime.utcnow())

  return app