from flask import Blueprint
from app.util.with_res import with_res
from app.util.validate_req import validate
from app.queries.v1 import auth as auth_sql
from voluptuous import Schema, REMOVE_EXTRA

auth_bp_v1 = Blueprint('auth_bp_v1', __name__)

@auth_bp_v1.route("/register")
@with_res
@validate(Schema({
  'a': str,
  'b': int,
}, extra=REMOVE_EXTRA))
def register(req_body, res):
  try:
    res.set_data(req_body)
    res.message = "It's good!"
  except BaseException as e:
    res.add_error(e)
  finally:
    return res.json()
