from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.util.custom_api_response import with_res
from app.util.validations.view_decorator import validate

from app.util.request_schemas import ReqSchema
from app.db import Query

import app.queries.v1.action_category as db


action_category_bp_v1 = Blueprint("action_category_bp_v1", __name__)

@action_category_bp_v1.route("/", methods=["GET", "POST", "PUT", "DELETE"])
@jwt_required
@with_res
def action_category_view(res):
  try:
    user_id = get_jwt_identity()
    if request.method == "GET":
      res.add_data({ 
        'action_categories': db.select_category_by_user(user_id) 
      })

    elif request.method == "POST":
      category = ReqSchema.new_action_category(request.get_json())
      if not db.user_action_category_exists(user_id, category["category_name"]):
        db.insert_action_category(user_id, category["category_name"])
      res.add_data({ 
        'action_categories': db.select_category_by_user(user_id)
      })
      res.status = 201
    
    elif request.method == "PUT":
      category = ReqSchema.update_action_category(request.get_json())
      Query.do_update(
        "action_category",
        update_data={ key: category[key] for key in category.keys() if key != "id" },
        condition_data={ "id": category["id"], "user_id": user_id }
      )
      res.status = 201

    elif request.method == "DELETE":
      category = ReqSchema.update_action_category(request.args)
      Query.do_delete(
        "action_category", 
        condition_data={ "id": category["id"], "user_id": user_id }
      )

  except BaseException as e:
    print(e)
    res.add_error(e)
  finally:
    return res
