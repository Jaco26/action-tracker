import uuid
from datetime import datetime

def UUID(val):
  return uuid.UUID(val)

def Timestamp(val):
  return datetime.strftime("%Y-%m-%d %H:%M:%S.%f")


print(datetime.strptime("2019-03-20T02:19:28.203Z", "%Y-%m-%dT%H:%M:%S.%f%z"))