from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from psycopg2.extras import DateTimeTZRange

from app.queries.v1 import action_taken
from app.db import Query, do_select, do_insert, do_update, do_delete

from app.util.custom_api_response import with_res
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
          'actions': action_taken.get_all_between_dates(user_id, start_d, end_end_of_day),
        })
      else:
        res.add_data({
          'actions': action_taken.get_all(user_id),
        })

    elif request.method == "POST":
      action = ReqSchema.new_action(request.get_json())
      action.update({ "user_id": user_id })
      duration = action.get("duration")
      if duration:
        data = {
          "duration": DateTimeTZRange(duration["start_time"], duration["end_time"]),
          **{ key: action[key] for key in action.keys() if key != "duration" } 
        }
        Query.do_insert(
          "action_taken",
          data=data,
          colnames_text="user_id, category_id, description, duration",
          values_text="%(user_id)s, %(category_id)s, %(description)s, %(duration)s"
        )
      else:
        Query.do_insert("action_taken", data=action)
      res.status = 201
   

    elif request.method == "PUT":
      action = ReqSchema.action_update(request.get_json())
      do_update(
        tablename="action_taken", 
        update_data=action, 
        condition="id = %(id)s AND user_id = %(user_id)s",
        condition_data={ "user_id": user_id }
      )

    elif request.method == "DELETE":
      action = ReqSchema.action_update(request.get_json())
      do_delete(
        tablename="action_taken", 
        condition="id = %(id)s AND user_id = %(user_id)s", 
        condition_data={ 
          "id": action["id"],
          "user_id": user_id,
        }  
      )

  except BaseException as e:
    res.add_error(e)

  finally:
    return res