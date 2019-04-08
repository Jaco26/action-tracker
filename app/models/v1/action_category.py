from sqlalchemy import text
from fsa_db import db

user_action_category = db.Table("user_action_category",
  db.Column("user_id", db.UUIDtype, db.ForeignKey("users.id"), primary_key=True),
  db.Column("category_id", db.UUIDtype, db.ForeignKey("action_category.id"), primary_key=True)
)

class ActionCategory(db.Model):
  __tablename__ = "action_category"

  id = db.Column(db.UUIDtype, server_default=text("generate_uuid_v4()"), primary_key=True)
  category_name = db.Column(db.String(), uniuque=True, nullable=False)
