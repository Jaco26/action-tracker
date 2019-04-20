import uuid
from voluptuous import Schema, All, Required, Date, REMOVE_EXTRA

class DateFormats:
  date = "%Y-%m-%d"
  timestamptz = "%Y-%m-%dT%H:%M:%S.%f%z"

class CustomValidators:
  UUID = lambda val: str(uuid.UUID(val))


class ReqSchema:
  tstz_range = Schema({
    Required("start"): Date(DateFormats.timestamptz),
    Required("end"): Date(DateFormats.timestamptz),
  }, REMOVE_EXTRA)

  date_range = Schema({
    Required("start"): Date(DateFormats.timestamptz),
    Required("end"): Date(DateFormats.timestamptz),
  }, REMOVE_EXTRA)

  new_action = Schema({
    Required("id"): CustomValidators.UUID,
    Required("category_id"): CustomValidators.UUID,
    "description": str,
    "ts_override": Date(DateFormats.timestamptz),
    "duration": ReqSchema.tstz_range
  }, REMOVE_EXTRA)
