import datetime
from werkzeug.exceptions import HTTPException, default_exceptions
from flask import Blueprint, abort
from flask_jwt_extended import (
  jwt_required, jwt_refresh_token_required, create_access_token,
  create_refresh_token, get_jwt_identity, get_raw_jwt
)
from werkzeug.security import generate_password_hash, check_password_hash
from app.util.custom_api_response import with_res
from app.util.validations.view_decorator import validate
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
        res.add_data({
          'access_token': create_access_token(identity=user.get("id"), expires_delta=False), # expires in 2 hours
          'refresh_token': create_refresh_token(identity=user.get("id")),
          'username': username,
        })
        res.message = "You're logged in!"
      else:
        abort(403)
    else:
      abort(403)
  except BaseException as e:
    res.add_error(e)
    res.status = e.code
  finally:
    return res


@auth_bp_v1.route("/refresh", methods=["POST"])
@jwt_refresh_token_required
@with_res
def refresh(res):
  try:
    res.add_data({ 
      'access_token': create_access_token(identity=get_jwt_identity(), expires_delta=datetime.timedelta(seconds=7200)), # expires in 2 hours
    })
  except BaseException as e:
    res.add_error(e)
  finally:
    return res


@auth_bp_v1.route("/logout-access", methods=["POST"])
@jwt_required
@with_res
def logout_access(res):
  try:
    jti = get_raw_jwt()['jti']
    auth_sql.revoke_jti(jti)
    res.message = "Access token revoked!"
  except BaseException as e:
    res.add_error(e, "Error revoking access token")
  finally:
    return res


@auth_bp_v1.route("/logout-refresh", methods=["POST"])
@jwt_refresh_token_required
@with_res
def logout_refresh(res):
  try:
    jti = get_raw_jwt()['jti']
    auth_sql.revoke_jti(jti)
    res.message = "Refresh token revoked!"
  except BaseException as e:
    res.add_error(e, "Error revoking refresh token")
  finally:
    return res