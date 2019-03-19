from datetime import datetime

class Action:
  def __init__(self, *args, **fields):
    utc_now = datetime.utcnow()

    self.id = fields.get("id", "")
    self.category_id = fields.get("category_id", "")
    self.duration = fields.get("duration", "")
    self.ts = fields.get("ts", datetime.strftime(utc_now, "%Y-%m-%d %H:%M:%S.%f"))
    self.description = fields.get("description", "")

