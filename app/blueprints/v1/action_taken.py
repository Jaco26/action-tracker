from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

import app.queries.v1.action_taken as db 
from app.queries.v1.action_taken import do_insert

from app.util.custom_api_response import with_res
from app.util.validations.view_decorator import validate
# from app.util.validations.schemas import date_range_schema, create_action_schema
from app.util.request_schemas import ReqSchema


from datetime import datetime, timedelta

action_taken_bp_v1 = Blueprint('action_taken_bp_v1', __name__)

@action_taken_bp_v1.route("/", methods=["GET", "POST", "PUT", "DELETE"])
@jwt_required
@with_res
def action_taken_view(res):
  try:
    user_id = get_jwt_identity()

    if request.method == "GET":
      date_range = ReqSchema.date_range(request.args)
      if date_range:
        start = date_range["start"]
        start_d = datetime.strptime(start, "%Y-%m-%d")
        end = date_range["end"]
        end_d = datetime.strptime(end, "%Y-%m-%d")

        end_end_of_day = end_d + timedelta(seconds=86399)
        res.add_data({
          'actions': db.get_all_between_dates(user_id, start_d, end_end_of_day),
        })
      else:
        res.add_data({
          'actions': db.get_all(user_id),
        })

    elif request.method == "POST":
      action = ReqSchema.new_action(request.get_json())
      # print("action", action)
      print("do_insert", do_insert("action_taken", {
        "user_id": user_id,
        **action
      }))
      # db.insert_action_taken(user_id, action)

    elif request.method == "PUT":
      db.update(user_id, action)

    elif request.method == "DELETE":
      db.delete(action["id"], user_id)

  except BaseException as e:
    res.add_error(e)

  finally:
    return res