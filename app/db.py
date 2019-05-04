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
  def __init__(self, ):
    self.pool = None
  
  def init_app(self, app):
    self.pool = ThreadedConnectionPool(
      minconn=1, 
      maxconn=10,
      dsn=app.config["DATABASE_URL"]
    )
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
                # print("SQL", sql)
                # print("FETCH ONE RESULT", result)
              if type(result) is list and not len(result):
                return []
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


pool = Pool()


class Query:

  @classmethod
  def custom_select(cls, mode="fetchall", sql="", values={}):
    @pool.execute(mode)
    def inner():
      return sql, values
    return inner()


  @classmethod
  @pool.execute()
  def simple_select(cls, tablename="", condition_data={}):
    condition_keys = condition_data.keys()
    condition_text = " AND ".join([f"{colname} = %({colname})s" for colname in condition_keys])
  
    sql = f"SELECT * FROM {tablename} WHERE {condition_text}"
    values = { colname: condition_data[colname] for colname in condition_keys }

    return sql, values
  

  @classmethod
  @pool.execute()
  def do_insert(cls, tablename="", data={}, colnames_text=None, values_text=None):
    data_keys = data.keys()

    if not colnames_text:
      colnames_text = ", ".join([f"{colname}" for colname in data_keys])

    if not values_text:
      values_text = ", ".join([f"%({colname})s" for colname in data_keys])

    sql = f"INSERT INTO {tablename} ({colnames_text}) VALUES({values_text});"
    values = { key: data[key] for key in data_keys }

    return sql, values


  @classmethod
  @pool.execute()
  def do_update(cls, tablename="", update_data={}, condition_data={}, update_text=None, condition_text=None):
    update_keys = update_data.keys()
    condition_keys = condition_data.keys()

    all_values = { **update_data, **condition_data }

    if not update_text:
      colnames_text = ", ".join([f"{colname} = %({colname})s" for colname in update_keys])

    if not condition_text:
      condition_text = " AND ".join([f"{condition_key} = %({condition_key})s" for condition_key in condition_keys])

    sql = f"UPDATE {tablename} SET {colnames_text} WHERE {condition_text};"
    values = { key: all_values[key] for key in all_values.keys() }

    return sql, values


  @classmethod
  @pool.execute()
  def do_delete(cls, tablename="", condition_data={}, condition_text=None):
    condition_keys = condition_data.keys()

    if not condition_text:
      condition_text = " AND ".join([f"{condition_key} = %({condition_key})s" for condition_key in condition_keys])

    sql = f"DELETE FROM {tablename} WHERE {condition_text};"
    values = { key: condition_data[key] for key in condition_keys }

    return sql, values
      
