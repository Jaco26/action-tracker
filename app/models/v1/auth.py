
from sqlalchemy import text
from app.fsa_db import db


class RevokedToken(db.Model):

  jti = db.Column(db.String(), primary_key=True)

  def save_to_db(self):
    db.session.add(self)
    db.session.commit()



class User(db.Model):
  __tablename__ = "users"
  
  id = db.Column(db.UUIDtype, server_default=text("generate_uuid_v4()"), primary_key=True)
  role = db.Column(db.Integer, default=1)
  username = db.Column(db.String(), unique=True, nullable=False)
  pw_hash = db.Column(db.String(), nullable=False)

  @classmethod
  def find_by_username(cls, username):
    return cls.query.filter_by(username=username).first()

  def save_to_db(self):
    db.session.add(self)
    db.session.commit()



  
  

  

  

