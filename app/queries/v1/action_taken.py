from datetime import datetime
from app.db import pool
from app.util.json_encoder import SimpleUTC


@pool.execute()
def get_all(user_id):
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
def get_all_between_dates(user_id, d1, d2):
  sql = """SELECT * FROM action_taken 
           WHERE user_id = %s AND date_trunc('hour', ts) 
           BETWEEN %s AND %s;"""
  return sql, [user_id, d1, d2]
  