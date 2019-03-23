from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.queries.v1 import action_taken
from app.util.custom_api_response import with_res
from app.util.validations.view_decorator import validate
from app.util.validations.schemas import date_range_schema, action_schema

from datetime import datetime, timedelta

action_taken_bp_v1 = Blueprint('action_taken_bp_v1', __name__)

@action_taken_bp_v1.route("/", methods=["GET", "POST", "PUT", "DELETE"])
@jwt_required
@with_res
def action_taken_view(res):
  try:
    user_id = get_jwt_identity()
    action = action_schema(request.get_json()["action"]) if request.get_json() else None
    date_range = date_range_schema(dict(request.args)) if request.args else None

    if request.method == "GET":
      if date_range:
        start = date_range["start"]
        start_d = datetime.strptime(start, "%Y-%m-%d")
        end = date_range["end"]
        end_d = datetime.strptime(end, "%Y-%m-%d")

        end_end_of_day = end_d + timedelta(seconds=86399)
        print(start_d, end_end_of_day)
        res.add_data({
          'actions': action_taken.get_all_between_dates(user_id, start_d, end_end_of_day),
        })
      else:
        res.add_data({
          'actions': action_taken.get_all(user_id),
        })

    elif request.method == "POST":
      action_taken.create(user_id, action)

    elif request.method == "PUT":
      action_taken.update(user_id, action)

    elif request.method == "DELETE":
      action_taken.delete(action["id"], user_id)

  except BaseException as e:
    res.add_error(e)

  finally:
    return res