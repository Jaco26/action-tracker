import os
import dotenv
import functools
import psycopg2
import json
from datetime import date
from psycopg2.extras import RealDictCursor

dotenv.load_dotenv()

# convert datetime objects returned by psycopg2 into str
class DateEncoder(json.JSONEncoder):
  def default(self, obj):
    if isinstance(obj, date):
      return str(obj)
    return json.JSONEncoder.default(self, obj)


class DB:
  def __init__(self, db_uri):
    self.db_uri = db_uri
  
  def execute(self, func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
      with psycopg2.connect(self.db_uri) as conn:
        with conn.cursor(cursor_factory=RealDictCursor) as c:
          sql, values = func(*args, **kwargs)
          c.execute(sql, values)
          result = [json.dumps(x, cls=DateEncoder) for x in c.fetchall()] if sql.strip().upper().startswith("SELECT") else None
      conn.close()
      return result
    return wrapper

  def executemany(self, func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
      with psycopg2.connect(self.db_uri) as conn:
        with conn.cursor() as c:
          sql, values = func(*args, **kwargs)
          c.executemany(sql, values)
      conn.close()
      return True
    return wrapper
