from flask import Flask, jsonify
from datetime import datetime

from .util.json_encoder import CustomJSONEncoder

def create_app():
  app = Flask(__name__)
  app.json_encoder = CustomJSONEncoder

  @app.route("/")
  def index():
    return jsonify(message="Hello You!", date=datetime.utcnow())

  return app