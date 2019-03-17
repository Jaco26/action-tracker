from flask_jwt_extended import JWTManager
from app.queries.v1 import auth as auth_sql

def init_app(app):
  jwt = JWTManager(app)
  
  @jwt.token_in_blacklist_loader
  def is_token_revoked(decryped_token):
    jti = decryped_token.get('jti')
    return bool(auth_sql.get_jti(jti))
