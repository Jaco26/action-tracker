from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.queries.v1 import action_category
from app.util.custom_api_response import with_res
from app.util.validations.view_decorator import validate


action_category_bp_v1 = Blueprint("action_category_bp_v1", __name__)

@action_category_bp_v1.route("/", methods=["GET", "POST", "PUT", "DELETE"])
@jwt_required
@with_res
@validate({
  "category_name": str,
  "category_id": str,
  "new_category_name": str,
})
def action_category_view(req_body, res):
  try:
    user_id = get_jwt_identity()
    if request.method == "GET":
      bla = action_category.get_all(user_id) 
      print(bla)
      res.add_data({ 
        'action_categories': action_category.get_all(user_id) 
      })

    elif request.method == "POST":
      category_name = req_body.get("category_name")
      print('cattttttt', category_name)
      action_category.create(user_id, category_name)
      res.add_data({ 
        'action_categories': action_category.get_all(user_id) 
      })
    
    elif request.method == "PUT":
      new_category_name = req_body.get("new_category_name")
      category_id = req_body.get("category_id")
      action_category.update(new_category_name, category_id, user_id)
      res.add_data({ 
        'action_categories': action_category.get_all(user_id) 
      })

    elif request.method == "DELETE":
      category_id = req_body.get("category_id")
      action_category.delete(category_id, user_id)
      res.add_data({ 
        'action_categories': action_category.get_all(user_id) 
      })
  except BaseException as e:
    res.add_error(e)
  finally:
    return res
