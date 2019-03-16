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
    if type(items) is str:
      return items, []
    elif type(items) is tuple:
      if len(items) == 1:
        return items[0], []
      else:
        return items[0], items[1]

  def execute(self, cursor_method="fetchall"):
    def decorator(func):
      @functools.wraps(func)
      def wrapper(*args, **kwargs):
        with self.get_conn() as conn:
          with conn.cursor(cursor_factory=RealDictCursor) as c:
            sql, values = self.unwrap_pg_statement(func, *args, **kwargs)
            c.execute(sql, values)
            if sql.strip().upper().startswith("SELECT"):
              if cursor_method == "fetchall":
                result = [x for x in c.fetchall()]
              elif cursor_method == "fetchone":
                result = c.fetchone()
              if type(result) is list and len(result):
                return None
              return result
            return True
      return wrapper
    return decorator

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
