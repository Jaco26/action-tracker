import functools
from flask import request, abort
from voluptuous import Schema, Invalid, REMOVE_EXTRA

def validate(schema_dict):
  schema = Schema(schema_dict, extra=REMOVE_EXTRA)
  def decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
      try:
        req_body = schema(request.get_json())
      except Invalid as e:
        abort(401, str(e))
      return func(req_body, *args, **kwargs)
    return wrapper
  return decorator