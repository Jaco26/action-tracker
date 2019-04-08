import os
from datetime import datetime
from my_migrations.lib import Manager

manager = Manager(os.environ.get("DATABASE_URL"))

up = """
    Hi how are you;
    I am doing pretty good;
    how about you;
    """

down = """
    Oh I am good too;
    It is a nice day huh;
    """

if __name__ == "__main__":
  # manager.create_migration({
  #   "version_name": "Jacob's version",
  #   "upgrade_text": up,
  #   "downgrade_text": down,
  # })
  manager.execute_migration("up")
