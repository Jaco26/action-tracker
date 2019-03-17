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


@auth_bp_v1.route("/login", methods=["POST"])
@with_res
@validate({
  'username': str,
  'password': str,
})
def login(req_body, res):
  try:
    username = req_body.get("username")
    user = auth_sql.get_user_by_username(username)
    if user:
      if check_password_hash(user.get("pw_hash"), req_body.get("password")):
        res.set_data({
          'access_token': create_access_token(identity=user.get("id")),
          'refresh_token': create_refresh_token(identity=user.get("id")),
        })
        res.message = "You're logged in!"
  except BaseException as e:
    res.add_error(e)
  finally:
    return res


@auth_bp_v1.route("/refresh", methods=["POST"])
@jwt_refresh_token_required
@with_res
def refresh(res):
  res.set_data({ 'access_token': create_access_token(identity=get_jwt_identity()) })
  return res