from flask import Flask, jsonify
from datetime import datetime

from .util.json_encoder import CustomJSONEncoder
from .db import pool
from .queries import create_tables

def create_app():
  app = Flask(__name__)
  app.json_encoder = CustomJSONEncoder

  pool.init_app(app)

  @app.before_first_request
  def do_before():
    create_tables.create_tables()

  @app.route("/")
  def index():
    return jsonify(message="Hello You!", date=datetime.utcnow())

  return app