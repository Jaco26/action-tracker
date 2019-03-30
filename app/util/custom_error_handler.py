from flask import jsonify
from werkzeug.exceptions import HTTPException, default_exceptions

class CustomErrorHandler:
  def jsonify_default_exceptions(self, error):

    if isinstance(error, HTTPException):
      result = {
        'code': error.code,
        # 'description': error.description,
        'message': str(error),
      }
    else:
      result = {
        'code': 500,
        # 'description': error.description,
        'message': str(error),
      }
    res = jsonify(result)
    res.status_code = result['code']
    return res

  def init_app(self, app):
    for code in default_exceptions.keys():
      app.register_error_handler(code, self.jsonify_default_exceptions)


custom_error_handler = CustomErrorHandler()