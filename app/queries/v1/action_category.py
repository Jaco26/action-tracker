from app.db import pool

@pool.execute()
def create(user_id, category_name):
  sql = "INSERT INTO action_category (user_id, category_name) VALUES (%s, %s);"
  return sql, [user_id, category_name]

@pool.execute()
def update(new_category_name, category_id, user_id):
  sql = "UPDATE action_category SET category_name = %s WHERE id = %s AND user_id = %s;"
  return sql, [new_category_name, category_id, user_id]
  
@pool.execute()
def delete(category_id, user_id):
  sql = "DELETE FROM action_category WHERE id = %s AND user_id = %s;"
  return sql, [category_id, user_id]

@pool.execute()
def get_all(user_id):
  return "SELECT id, category_name FROM action_category WHERE user_id = %s;", [user_id]

