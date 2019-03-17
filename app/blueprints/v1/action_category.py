from flask import Blueprint, request
from flask.views import MethodView
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.queries.v1 import action_category
from app.util.custom_api_response import with_res
from app.util.validate_req import validate, Optional


action_category_bp_v1 = Blueprint("action_category_bp_v1", __name__)

# class ActionCategory(MethodView):
#   decorators = [jwt_required, with_res]

#   # @jwt_required
#   # @with_res
#   def get(self, res):
#     try:
#       user_id = get_jwt_identity()
#       res.add_data({ 
#         'action_categories': action_category.get_all(user_id) 
#       })
#     except BaseException as e:
#       res.add_error(e)
#     finally:
#       return res


#   # @jwt_required
#   # @with_res
#   @validate({
#     'category_name': str,
#   })
#   def post(self, req_body, res):
#     try:
#       user_id = get_jwt_identity()
#       category_name = req_body.get("category_name")
#       action_category.create(user_id, category_name)
#       res.add_data({ 
#         'action_categories': action_category.get_all(user_id) 
#       })
#     except BaseException as e:
#       res.add_error(e)
#     finally:
#       return res


#   # @jwt_required
#   # @with_res
#   @validate({
#     'new_category_name': str,
#     'category_id': str,
#   })
#   def update(self, req_body, res):
#     try:
#       user_id = get_jwt_identity()
#       new_category_name = req_body.get("new_category_name")
#       category_id = req_body.get("category_id")
#       action_category.update(new_category_name, category_id, user_id)
#       res.add_data({ 
#         'action_categories': action_category.get_all(user_id) 
#       })
#     except BaseException as e:
#       res.add_error(e)
#     finally:
#       return res


#   # @jwt_required
#   # @with_res
#   @validate({
#     'category_id': str,
#   })
#   def delete(self, req_body, res):
#     try:
#       user_id = get_jwt_identity()
#       category_id = req_body.get("category_id")
#       action_category.delete(category_id, user_id)
#       res.add_data({ 
#         'action_categories': action_category.get_all(user_id) 
#       })
#     except BaseException as e:
#       res.add_error(e)
#     finally:
#       return res


@action_category_bp_v1.route("/", methods=["GET", "POST", "UPDATE", "DELETE"])
@jwt_required
@with_res
@validate({
  "category_name": Optional(str),
  "category_id": Optional(str),
  "new_category_name": Optional(str),
})
def create_action_category(req_body, res):
  try:
    user_id = get_jwt_identity()
    if request.method == "GET":
      res.add_data({ 
        'action_categories': action_category.get_all(user_id) 
      })

    elif request.method == "POST":
      category_name = req_body.get("category_name")
      action_category.create(user_id, category_name)
      res.add_data({ 
        'action_categories': action_category.get_all(user_id) 
      })
    
    elif request.method == "UPDATE":
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
