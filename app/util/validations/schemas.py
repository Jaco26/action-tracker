import uuid
from voluptuous import Schema, All, Required, Date

action = Schema({
  Required("id"): str,
  Required("category_id"): str,
  "duration": 
})


date_range = Schema({
  "start": Date('%Y-%m-%d')
})