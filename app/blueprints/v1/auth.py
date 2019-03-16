from flask import Blueprint
from app.util.with_res import with_res
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
    user = auth_sql.get_user_by_username(req_body.get('username'))
    res.set_data(user)
  except BaseException as e:
    res.add_error(e)
  finally:
    return res.json()
