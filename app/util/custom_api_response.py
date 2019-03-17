import functools
from flask import Flask, Response, jsonify, json


class ApiResult:
  def __init__(self, status=200):
    self.data = {}
    self.message = ""
    self.errors = []
    self.status = status

  def add_data(self, data):
    self.data.update(data)

  def add_error(self, error="", message=""):
    self.errors.append({
      "message": message, 
      "error": str(error)
    })

  def to_response(self):
    return jsonify(
      data=self.data,
      errors=self.errors,
      message=self.message,
      status=self.status,
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