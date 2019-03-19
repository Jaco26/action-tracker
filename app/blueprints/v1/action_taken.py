from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity


from app.queries.v1 import action_taken
from app.util.custom_api_response import with_res
from app.util.validate_req import validate
from app.util.validate_date_format import validate_dates

from app.util.req_body_types import Action

action_taken_bp_v1 = Blueprint('action_taken_bp_v1', __name__)

@action_taken_bp_v1.route("/", methods=["GET", "POST", "PUT", "DELETE"])
@jwt_required
@with_res
# @validate({
#   'action_id': str,
#   'category_id': str,
#   'duration': str,
#   'description': str,
#   'ts': str
# })
@validate({
  "action": {
    "id": str,
    "category_id": str,
    "duration": str,
    "description": str,
    "ts": str,
  }
})
def action_taken_view(req_body, res):
  
  try:
    user_id = get_jwt_identity()
    action = Action(req_body.get("action")).__dict__

    start_date = request.args.get("start_date")
    end_date = request.args.get("end_date")

    if request.method == "GET":
      if start_date and end_date:
        if validate_dates(start_date, end_date):
          res.add_data({
            'actions': action_taken.get_all_between_dates(user_id, start_date, end_date),
          })
        else:
          raise BaseException("the dates provided were invalid. please use format YYYY-MM-DD")
      else:
        res.add_data({
          'actions': action_taken.get_all(user_id),
        })

    elif request.method == "POST":
      action_taken.create(user_id, action)

    elif request.method == "PUT":
      action_taken.update(user_id, action)

    elif request.method == "DELETE":
      action_taken.delete(action["action_id"], user_id)

  except BaseException as e:
    res.add_error(e)

  finally:
    return res