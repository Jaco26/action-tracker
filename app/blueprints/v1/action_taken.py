from flask import Blueprint, request, abort
from flask_jwt_extended import jwt_required, get_jwt_identity
from psycopg2.extras import DateTimeTZRange

# from app.queries.v1 import action_taken
import app.queries.v1.action_taken as queries
from app.db import Query

from app.util.custom_api_response import with_res
from app.util.request_schemas import ReqSchema

from datetime import datetime, timedelta

action_taken_bp_v1 = Blueprint('action_taken_bp_v1', __name__)

GET_REQUEST_LIMIT = 200

@action_taken_bp_v1.route("/", methods=["GET", "POST", "PUT", "DELETE"])
@jwt_required
@with_res
def action_taken_view(res):
  try:
    user_id = get_jwt_identity()

    if request.method == "GET":      
      action_request = ReqSchema.get_actions(request.args)

      if action_request.get("start_date"):
        date_range = ReqSchema.date_range(request.args)
        start = date_range["start"]
        start_d = datetime.strptime(start, "%Y-%m-%d")
        end = date_range["end"]
        end_d = datetime.strptime(end, "%Y-%m-%d")


        end_end_of_day = end_d + timedelta(seconds=86399)
        res.add_data({
          'actions': action_taken.get_all_between_dates(user_id, start_d, end_end_of_day),
        })
      else:
        
        offset = action_request["offset"]
      
        result_count = queries.count_actions_taken_by(user_id).get("count")

        if result_count and result_count > offset + GET_REQUEST_LIMIT:
          res.next_page_url = f"/api/v1/action-taken/?offset={offset + GET_REQUEST_LIMIT}"

        res.add_data({
          "actions": queries.get_page_of_actions_taken_by(user_id, offset, GET_REQUEST_LIMIT)
        })
        res.result_count = result_count
        res.offset = offset
 

    elif request.method == "POST":
      action = ReqSchema.new_action(request.get_json())
      action.update({ "user_id": user_id })
      if action.get("duration"):
        action.update({
          "duration": DateTimeTZRange(action["duration"]["start_time"], action["duration"]["end_time"])
        })
      Query.do_insert("action_taken", data=action)
      res.status = 201
   

    elif request.method == "PUT":
      action = ReqSchema.action_update(request.get_json())
      if action.get("duration"):
        action.update({
          "duration": DateTimeTZRange(action["duration"]["start_time"], action["duration"]["end_time"])
        })
      Query.do_update(
        "action_taken", 
        update_data={ key: action[key] for key in action.keys() if key != "id" }, 
        condition_data={ "id": action["id"] }
      )
      res.status = 201

    elif request.method == "DELETE":
      action = ReqSchema.action_update(request.args)
      Query.do_delete(
        "action_taken", 
        condition_data={ "id": action["id"], "user_id": user_id }
      )

  except BaseException as e:
    print(e)
    res.add_error(e)

  finally:
    return res