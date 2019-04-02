from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.util.custom_api_response import with_res
from app.util.validations.view_decorator import validate

import app.queries.v1.action_category as db


action_category_bp_v1 = Blueprint("action_category_bp_v1", __name__)

@action_category_bp_v1.route("/", methods=["GET", "POST", "PUT", "DELETE"])
@action_category_bp_v1.route("/<uuid:category_id>", methods=["DELETE"])
@jwt_required
@with_res
@validate({
  "category_name": str,
  "category_id": str,
  "new_category_name": str,
})
def action_category_view(req_body, res, category_id=None):
  try:
    user_id = get_jwt_identity()
    if request.method == "GET":
      res.add_data({ 
        'action_categories': db.select_category_by_user(user_id) 
      })

    elif request.method == "POST":
      category_name = req_body.get("category_name")
      if not db.user_action_category_exists(user_id, category_name):
        db.insert_action_category(user_id, category_name)
      res.add_data({ 
        'action_categories': db.select_category_by_user(user_id)
      })
    
    elif request.method == "PUT":
      new_category_name = req_body.get("new_category_name")
      category_id = req_body.get("category_id")
      db.update_action_category(new_category_name, category_id, user_id)
  

    elif request.method == "DELETE":
      db.delete_from_action_category(str(category_id))
     
  except BaseException as e:
    print(e)
    res.add_error(e)
  finally:
    return res
