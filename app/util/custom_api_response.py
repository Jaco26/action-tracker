import functools
from flask import Flask, Response, json


class ApiResult:
  data = {}
  num_results = None
  offset = None

  errors = []
  message = ""
  status = 200

  def add_data(self, data):
    self.data.update(data)

  def add_error(self, error=""):
    self.errors.append(str(error))

  def to_response(self):
    return Response(
      json.dumps(dict(
        data=self.data,
        num_results=self.num_results,
        offset=self.offset,
        message=self.message,
        errors=self.errors
      )),
      status=self.status,
      mimetype="application/json"
    )


class ApiFlask(Flask):
  def make_response(self, rv):
    if isinstance(rv, ApiResult):
      return rv.to_response()
    return Flask.make_response(self, rv)

def with_res(func):
  @functools.wraps(func)
  def func_wrapper(*args, **kwargs):
    return func(ApiResult(), *args, **kwargs)
  return func_wrapper