import functools
from flask import request
from voluptuous import Invalid

def validate(schema):
  def decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
      try:
        req_body = schema(request.get_json())
      except Invalid as e:
        raise BaseException("Invalid request data!")
      return func(req_body, *args, **kwargs)
    return wrapper
  return decorator