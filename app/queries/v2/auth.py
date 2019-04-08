from app.fsa_db import db
from app.models.v1.auth import User, RevokedToken


def get_jti(jti):
  return RevokedToken.get(jti)

def revoke_jti(jti):
  revoked = RevokedToken(jti)
  revoked.save_to_db()

def get_user_by_username(username):
  return User.find_by_username(username)

def add_user(username, pw_hash):
  user = User(username, pw_hash)
  user.save_to_db()
