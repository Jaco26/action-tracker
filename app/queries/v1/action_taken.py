from app.db import pool

@pool.execute()
def create(user_id, duration, category_id, description):
  sql = """INSERT INTO action_taken (user_id, duration, category_id, description) 
           VALUES (%s, %s, %s, %s);"""
  return sql, [user_id, duration, category_id, description]


@pool.execute()
def update(col_to_update, new_value, action_id, user_id):
  sql = """
    UPDATE action_taken SET {col_to_update} = %s WHERE id = %s AND user_id = %s;
  """.format(col_to_update)
  return sql, [new_value, action_id, user_id]


@pool.execute()
def delete(action_id, user_id):
  return "DELETE FROM action_taken WHERE id = %s AND user_id = %s;", [action_id, user_id]


@pool.execute()
def get_all(user_id):
  return "SELECT * FROM action_taken WHERE user_id = %s;", [user_id]


@pool.execute()
def get_all_between_dates(user_id, d1, d2):
  sql = """SELECT * FROM action_taken 
           WHERE user_id = %s AND date_trunc('hour', ts) 
           BETWEEN %s AND %s;"""
  return sql, [user_id, d1, d2]
  



