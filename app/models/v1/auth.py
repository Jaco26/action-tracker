
from sqlalchemy import text
from app.fsa_db import db


class RevokedToken(db.Model):

  jti = db.Column(db.String(), primary_key=True)

  def insert(self):
    db.session.add(self)
    db.session.commit()



class User(db.Model):
  __tablename__ = "users"
  
  id = db.Column(db.UUIDtype, server_default=text("generate_uuid_v4()"), primary_key=True)
  role = db.Column(db.Integer)
  username = db.Column(db.String(), unique=True, nullable=False, index=True)
  password = db.Column(db.String(), nullable=False)

  def insert(self):
    db.session.add(self)
    db.session.commit()

  @classmethod
  def find_by_id(cls, _id):
    return cls.get(_id)

  @classmethod
  def find_by_username(cls, username):
    return cls.query.filter_by(username=username).first()

  @classmethod
  def delete(cls, _id):
    user = cls.get(_id)
    if user:
      db.session.delete(user)
      db.session.commit()


  
  

  

  

