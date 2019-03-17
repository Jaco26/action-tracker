from flask import Blueprint
from flask_jwt_extended import (
  jwt_required, jwt_refresh_token_required, create_access_token,
  create_refresh_token, get_jwt_identity, get_raw_jwt
)
from werkzeug.security import generate_password_hash, check_password_hash
from app.util.custom_api_response import with_res
from app.util.validate_req import validate
from app.queries.v1 import auth as auth_sql

auth_bp_v1 = Blueprint('auth_bp_v1', __name__)

@auth_bp_v1.route("/register", methods=["POST"])
@with_res
@validate({
  'username': str,
  'password': str,
})
def register(req_body, res):
  try:
    username = req_body.get('username')
    user = auth_sql.get_user_by_username(username)
    if user:
      res.add_error(message=f"User {username} already exists")
    else:
      pw_hash = generate_password_hash(req_body.get('password'))
      auth_sql.add_user(username, pw_hash)
      res.message = "You've successfully registered!"
  except BaseException as e:
    res.add_error(e)
  finally:
    return res


@auth_bp_v1.route("/", methods=["GET", "POST"])
def bla():
  res = ApiResult()
  res.add_error(message="Hi")
  return res