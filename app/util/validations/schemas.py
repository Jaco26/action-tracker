from voluptuous import Schema, All, Required, Date, REMOVE_EXTRA

from datetime import datetime
from app.util.validations.custom_validators import UUID


def CreateSchema(schema_dict):
  return Schema(schema_dict, extra=REMOVE_EXTRA)

class MyFormats:
  date = "%Y-%m-%d"
  timestamptz = "%Y-%m-%dT%H:%M:%S.%f%z"


tstz_range_schema = CreateSchema({
  Required("start"): Date(MyFormats.timestamptz),
  Required("end"): Date(MyFormats.timestamptz),
})


date_range_schema = CreateSchema({
  Required("start"): Date(MyFormats.date),
  Required("end"): Date(MyFormats.date),
})


action_schema = CreateSchema({
  Required("id"): UUID,
  Required("category_id"): UUID,
  "description": str,
  "ts": Date(MyFormats.timestamptz),
  "duration": tstz_range_schema,
})

create_action_schema = CreateSchema({
  Required("category_id"): UUID,
  "description": str,
  "ts": Date(MyFormats.timestamptz),
})


# time_range = CreateSchema({
#   "start_time": "2019-03-20T17:01:42.160020Z",
#   "end_time": "2019-03-20T23:02:10.140Z"
# })

# valid_range= date_range({
#   'start_date': '2018-2-28',
#   "end_date": "2019-03-20T23:02:10.140Z"
# })

