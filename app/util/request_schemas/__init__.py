import uuid
from voluptuous import Schema, All, Required, Date, REMOVE_EXTRA

class DateFormats:
  date = "%Y-%m-%d"
  timestamptz = "%Y-%m-%dT%H:%M:%S.%f%z"


class CustomValidators:
  UUID = lambda val: str(uuid.UUID(val))


def json_from(source, schema):
  return schema(dict(source)) if source else None


class ReqSchema:

  @classmethod
  def tstz_range(cls, source):
    return json_from(source, Schema({
      Required("start"): Date(DateFormats.timestamptz),
      Required("end"): Date(DateFormats.timestamptz),
    }, extra=REMOVE_EXTRA))

  @classmethod
  def date_range(cls, source):
    return json_from(source, Schema({
      Required("start"): Date(DateFormats.date),
      Required("end"): Date(DateFormats.date),
    }, extra=REMOVE_EXTRA))

  @classmethod
  def new_action(cls, source):
    return json_from(source, Schema({
      Required("user_id"): CustomValidators.UUID,
      Required("category_id"): CustomValidators.UUID,
      "description": str,
      "ts_override": Date(DateFormats.timestamptz),
      "duration": cls.tstz_range,
    }, extra=REMOVE_EXTRA))

