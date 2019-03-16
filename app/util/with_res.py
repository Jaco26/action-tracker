import functools
from flask import jsonify

# from app.util.validate_req import validate

class ApiResult(object):
  def __init__(self, data={}, message="", errors=[], status=200):
    self.data = data
    self.message = message
    self.errors = errors
    self.status = status

  def add_error(self, msg="", err=None):
    error = {"message": msg, "error": str(err)}
    self.errors.append(error)

  def set_data(self, results):
    self.data.update({"results": results})

  def json(self):
    return jsonify(
      data=self.data,
      errors=self.errors,
      message=self.message,
      status=self.status,
    )


def with_res(func):
  @functools.wraps(func)
  def func_wrapper(*args, **kwargs):
    return func(ApiResult(), *args, **kwargs)
  return func_wrapper