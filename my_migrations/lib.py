import os
import uuid
import psycopg2
import importlib
import re
from datetime import datetime



class Manager:

  ledger_sect_re = re.compile("---\nid:\s*(?P<id>.+)\ndate:\s*(?P<date>.+)\ndescription:\s*(?P<description>.+)\n---")

  def __init__(self, db_uri):
    self.db_uri = db_uri
    self.directory = os.path.dirname(os.path.abspath(__file__))

  def execute_sql(self, sql):
    with psycopg2.connect(self.db_uri) as conn:
      with conn.cursor() as c:
        c.execute(sql)
    conn.close()

  def write_history(self, *lines):
    with open(f"{self.directory}/history.txt", "a") as history_f:
      for line in lines:
        history_f.write(line)

  def create_migration(self, description, up_text, down_text):
    meta = {
      "id": uuid.uuid4().hex,
      "date_created": datetime.utcnow().isoformat(),
    }

    with open(f"{self.directory}/template.txt", "r") as template_f:
      with open(f"{self.directory}/versions/{meta['id']}.py", "w") as target_f:
        # Read template file into string
        template_str = template_f.read()
        # Replace appropriate items in the template string
        template_str = template_str.replace("%description%", description)
        template_str = template_str.replace("%id%", meta["id"])
        template_str = template_str.replace("%date_created%", meta["date_created"])
        template_str = template_str.replace("%upgrade_text%", up_text)
        template_str = template_str.replace("%downgrade_text%", down_text)
        # write updated template string to target file
        target_f.write(template_str)

    with open(f"{self.directory}/ledger.txt", "a") as ledger_f:
      ledger_f.write("\n")
      ledger_f.write("-----" * 9 + "\n")
      ledger_f.write(f"id:          {meta['id']}\n")
      ledger_f.write(f"date:        {meta['date_created']}\n")
      ledger_f.write(f"description: {description}\n")
      ledger_f.write("-----" * 9 + "\n")
    
    self.write_history(f"migration <{meta['id']}> created: {meta['date_created']}\n")

  def read_ledger(self):
    with open(f"{self.directory}/ledger.txt", "r") as ledger_f:
      print(ledger_f.read())
  
  def read_history(self):
    with open(f"{self.directory}/history.txt", "r") as history_f:
      print(history_f.read())
     
  def get_ledger_item(self, migration_id=None):
    with open(f"{self.directory}/ledger.txt", "r") as ledger_f:
      ledger_str = ledger_f.read()
      migrations = [m.groupdict() for m in self.ledger_sect_re.finditer(ledger_str)]
      if migration_id:
        the_migration = (next(iter(m for m in migrations if m["id"] == migration_id), None))
      else:
        the_migration = (migrations[-1])
      return the_migration

  def get_migration_script_module(self, migration_id):
    return importlib.import_module(f"my_migrations.versions.{migration_id}")
    
  def upgrade(self, migration_id=None):
    if not migration_id:
      migration_ledger_item = self.get_ledger_item(migration_id=None)
      migration_id = migration_ledger_item["id"]
    script_module = self.get_migration_script_module(migration_id)
    print(script_module.upgrade())

  def downgrade(self, migration_id=None):
    if not migration_id:
      migration_ledger_item = self.get_ledger_item(migration_id=None)
      migration_id = migration_ledger_item["id"]
    script_module = self.get_migration_script_module(migration_id)
    print(script_module.downgrade())
