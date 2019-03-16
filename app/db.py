import os
import dotenv
import functools
import psycopg2
import json
from datetime import date
from psycopg2.extras import RealDictCursor
from psycopg2.pool import ThreadedConnectionPool
from flask import g

dotenv.load_dotenv()

# convert datetime objects returned by psycopg2 into str
class CustomDateEncoder(json.JSONEncoder):
  def default(self, obj):
    if isinstance(obj, date):
      return str(obj)
    return json.JSONEncoder.default(self, obj)


class Pool:
  def __init__(self, db_uri):
    self.pool = ThreadedConnectionPool(
      minconn=10, 
      maxconn=20,
      dsn=db_uri
    )
  
  def init_app(self, app):
    app.teardown_appcontext(self.return_conn)

  def get_conn(self):
    if 'db_conn' not in g:
      g.db_conn = self.pool.getconn()
    return g.db_conn

  def return_conn(self, x):
    db_conn = g.pop('db_conn', None)
    if db_conn:
      self.pool.putconn(db_conn)

  def unwrap_pg_statement(self, func, *args, **kwargs):
    items = func(*args, **kwargs)
    print(type(items))
    if type(items) is str:
      return items, []
    elif type(items) is tuple:
      if len(items) == 1:
        return items[0], []
      else:
        return items[0], items[1]

  def execute(self, func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
      with self.get_conn() as conn:
        with conn.cursor(cursor_factory=RealDictCursor) as c:
          sql, values = self.unwrap_pg_statement(func, *args, **kwargs)
          c.execute(sql, values)
          return[json.dumps(x, cls=CustomDateEncoder) for x in c.fetchall()] if sql.strip().upper().startswith("SELECT") else True
    return wrapper

  def executemany(self, func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
      with self.get_conn() as conn:
        with conn.cursor() as c:
          sql, values = self.unwrap_pg_statement(func, *args, **kwargs)
          c.executemany(sql, values)
          return True
    return wrapper


pool = Pool(os.environ['DB_URI'])
