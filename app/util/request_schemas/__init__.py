import uuid
from psycopg2.extras import DateTimeTZRange
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
  def login_or_register(cls, source):
    return json_from(source, Schema({
      Required("username"): str,
      Required("password"): str,
    }, extra=REMOVE_EXTRA))

  @classmethod
  def tstz_range(cls, source):
    return json_from(source, Schema({
      Required("start_time"): Date(DateFormats.timestamptz),
      Required("end_time"): Date(DateFormats.timestamptz),
    }, extra=REMOVE_EXTRA))

  @classmethod
  def date_range(cls, source):
    return json_from(source, Schema({
      Required("start_date"): Date(DateFormats.date),
      Required("end_date"): Date(DateFormats.date),
    }, extra=REMOVE_EXTRA))

  @classmethod
  def new_action_category(cls, source):
    return json_from(source, Schema({
      Required("category_name"): str,
    }, extra=REMOVE_EXTRA))

  @classmethod
  def update_action_category(cls, source):
    return json_from(source, Schema({
      Required("id"): CustomValidators.UUID,
      "category_name": str,
    }, extra=REMOVE_EXTRA))

  @classmethod
  def new_action(cls, source):
    return json_from(source, Schema({
      Required("category_id"): CustomValidators.UUID,
      "description": str,
      "duration": cls.tstz_range
    }, extra=REMOVE_EXTRA))

  @classmethod
  def action_update(cls, source):
    return json_from(source, Schema({
      Required("id"): CustomValidators.UUID,
      "user_id": CustomValidators.UUID,
      "category_id": CustomValidators.UUID,
      "description": str,
      "duration": cls.tstz_range,
    }, extra=REMOVE_EXTRA))

