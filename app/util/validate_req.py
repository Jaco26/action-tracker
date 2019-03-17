import functools
from flask import request, abort
from voluptuous import Schema, Invalid, REMOVE_EXTRA, Optional

def validate(schema_dict={}):
  schema = Schema(schema_dict, extra=REMOVE_EXTRA)
  def decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
      try:
        req_json = request.get_json()
        if req_json:
          req_body = schema(req_json)
        else:
          req_body = {}
      except Invalid as e:
        abort(401, str(e))
      return func(req_body, *args, **kwargs)
    return wrapper
  return decorator