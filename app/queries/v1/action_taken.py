from app.db import pool

@pool.execute()
def create(user_id, action):
  print(user_id)
  sql = """INSERT INTO action_taken (user_id, ts, category_id, description) 
           VALUES (%s, %s, %s, %s);"""
  return sql, [user_id, action["ts"], action["category_id"], action["description"]]


@pool.execute()
def update(user_id, action):
  sql = """UPDATE action_taken SET ts = %s, category_id = %s, description = %s
           WHERE id = %s AND user_id = %s;""".format(col_to_update)
  return sql, [action["ts"], action["category_id"], action["description"], action["action_id"], user_id]


@pool.execute()
def delete(action_id, user_id):
  return "DELETE FROM action_taken WHERE id = %s AND user_id = %s;", [action_id, user_id]


@pool.execute()
def get_all(user_id):
  sql = """SELECT ac.category_name, at.description, at.ts, at.id 
           FROM action_taken AS at JOIN action_category AS ac 
           ON at.category_id = ac.id 
           WHERE at.user_id = %s;"""
  return sql, [user_id]


@pool.execute()
def get_all_between_dates(user_id, d1, d2):
  sql = """SELECT * FROM action_taken 
           WHERE user_id = %s AND date_trunc('day', ts) 
           BETWEEN %s AND %s;"""
  return sql, [user_id, d1, d2]
  



