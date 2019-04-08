from app.fsa_db import db

class ActionTaken(db.Model):
  
  id = db.Column(db.UUIDtype, primary_key=True, server_default="uuid_generate_v4()")
  