from app.db import pool

@pool.execute()
def get_jti(jti):
  return "SELECT * FROM revoked_token WHERE jti = %s;", [jti]

@pool.execute()
def save_jti(jti):
  return "INSERT INTO revoked_token (jti) VALUES (%s);", [jti]

@pool.execute(cursor_method="fetchone")
def get_user_by_username(username):
  return "SELECT * FROM users WHERE username = %s;", [username]

