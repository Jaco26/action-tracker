import functools
from flask import Flask, Response, json


class ApiResult:
  def __init__(self):
    self.data = {}
    self.result_count = None
    self.offset = None
    self.next_page_url = None

    self.errors = []
    self.message = ""
    self.status = 200

  def add_data(self, data):
    self.data.update(data)

  def add_error(self, error=""):
    self.errors.append(str(error))

  def to_response(self):
    return Response(
      json.dumps(dict(
        data=self.data,
        result_count=self.result_count,
        offset=self.offset,
        next_page_url=self.next_page_url,
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