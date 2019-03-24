from app.db import pool

@pool.execute(cursor_method="fetchone")
def user_action_category_exists(user_id, category_name):
  sql = "SELECT * FROM action_category WHERE user_id = %s AND category_name = %s;"
  return sql, [user_id, category_name]

@pool.execute()
def insert_action_category(user_id, category_name):
  sql = "INSERT INTO action_category (user_id, category_name) VALUES (%s, %s);" 
  return sql, [user_id, category_name]


@pool.execute()
def update_action_category(new_category_name, category_id, user_id):
  sql = "UPDATE action_category SET category_name = %s WHERE id = %s AND user_id = %s;"
  return sql, [new_category_name, category_id, user_id]
  

@pool.execute()
def delete_from_action_category(category_id):
  sql = """
    DELETE FROM action_taken WHERE category_id = %(id)s;
    DELETE FROM action_category WHERE id = %(id)s;
  """
  return sql, { "id": category_id }


@pool.execute()
def select_category_by_user(user_id):
  return "SELECT id, category_name FROM action_category WHERE user_id = %s;", [user_id]

