from flask.json import JSONEncoder
from datetime import date

class CustomJSONEncoder(JSONEncoder):
  def default(self, obj):
    if isinstance(obj, date):
      return obj.isoformat()
    return JSONEncoder.default(obj)
