from flask.json import JSONEncoder
from datetime import date, tzinfo, timedelta

class SimpleUTC(tzinfo):
    def tzname(self,**kwargs):
        return "UTC"
    def utcoffset(self, dt):
        return timedelta(0)


class CustomJSONEncoder(JSONEncoder):
  def default(self, obj):
    if isinstance(obj, date):
      return obj.replace(tzinfo=SimpleUTC()).isoformat()
    return JSONEncoder.default(obj)
