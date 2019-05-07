from datetime import datetime
from app.db import pool
from app.util.json_encoder import SimpleUTC


@pool.execute()
def get_all_actions_taken_by(user_id):
  sql = """SELECT 
            ac.category_name, 
            at.description, 
            at.ts AS time_saved,  
            at.id, 
            upper(at.duration) - lower(at.duration) as time_taken,
            upper(at.duration) AS end_time,
            lower(at.duration) AS start_time
           FROM action_taken AS at JOIN action_category AS ac 
           ON at.category_id = ac.id 
           WHERE at.user_id = %s;"""
  return sql, [user_id]


@pool.execute()
def get_page_of_actions_taken_by(user_id, offset, limit):
  sql = """SELECT 
            ac.category_name, 
            at.description, 
            at.ts AS time_saved,  
            at.id, 
            upper(at.duration) - lower(at.duration) as time_taken,
            upper(at.duration) AS end_time,
            lower(at.duration) AS start_time
           FROM action_taken AS at JOIN action_category AS ac 
           ON at.category_id = ac.id 
           WHERE at.user_id = %(user_id)s
           LIMIT %(limit)s OFFSET %(offset)s;"""
  return sql, { "user_id": user_id, "offset": offset, "limit": limit }

@pool.execute(cursor_method="fetchone")
def count_actions_taken_by(user_id):
  sql = "SELECT COUNT(id) FROM action_taken WHERE user_id = %s;"
  return sql, [user_id]


@pool.execute()
def count_all_between_dates(user_id, start_date, end_date):
  sql = """SELECT COUNT(id) FROM action_taken
            WHERE user_id = %(user_id)s
            AND ts BETWEEN %(start_date)s AND %(end_date)s;"""
  return sql, { "user_id": user_id, "start_date": start_date, "end_date": end_date }


@pool.execute()
def get_all_between_dates(user_id, d1, d2):
  sql = """SELECT * FROM action_taken 
           WHERE user_id = %s AND date_trunc('hour', ts) 
           BETWEEN %s AND %s;"""
  return sql, [user_id, d1, d2]
  