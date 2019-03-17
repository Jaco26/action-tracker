import re

date_re = re.compile('^(\d{4}-\d{1,2}-\d{1,2})$')

def validate_dates(*dates):
  for d in dates:
    if date_re.search(d) is None:
      return False
  return True