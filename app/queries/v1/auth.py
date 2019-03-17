from app.db import pool

@pool.execute(cursor_method="fetchone")
def get_jti(jti):
  return "SELECT * FROM revoked_token WHERE jti = %s;", [jti]

@pool.execute()
def revoke_jti(jti):
  return "INSERT INTO revoked_token (jti) VALUES (%s);", [jti]

@pool.execute(cursor_method="fetchone")
def get_user_by_username(username):
  return "SELECT * FROM users WHERE username = %s;", [username]

@pool.execute()
def add_user(username, pw_hash):
  return "INSERT INTO users (username, pw_hash) VALUES (%s, %s);", [username, pw_hash]

