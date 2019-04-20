import os
import uuid
import psycopg2
import importlib
import re
from datetime import datetime



class Manager:

  ledger_sect_re = re.compile(r"---\nid:\s*(?P<id>.+)\ndate:\s*(?P<date>.+)\ndescription:\s*(?P<description>.+)\n---")

  def __init__(self, db_uri):
    self.db_uri = db_uri
    self.db_name = db_uri[db_uri.rfind("/") + 1:]
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

    if type(up_text) is list:
      up_text = "".join(up_text)

    if type(down_text) is list:
      down_text = "".join(down_text)
      
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
    
    self.write_history(f"migration <{meta['id']}> CREATED: {meta['date_created']}\n")

  def get_file_text(self, filename):
    with open(f"{self.directory}/{filename}", "r") as file:
      return file.read()

  def versions(self):
    print(self.get_file_text("ledger.txt"))
  
  def logs(self):
    print(self.get_file_text("history.txt"))
     
  def get_ledger_item(self, migration_id=None):
    ledger_str = self.get_file_text("ledger.txt")
    migrations = [m.groupdict() for m in self.ledger_sect_re.finditer(ledger_str)]
    if migration_id:
      the_migration = (next(iter(m for m in migrations if m["id"] == migration_id), None))
    else:
      the_migration = (migrations[-1])
    return the_migration

  def get_migration_script_module(self, migration_id):
    return importlib.import_module(f"my_migrations.versions.{migration_id}")
  
  def migration_has_been_executed(self, migration_id="", direction=""):
    search_pattern = f"(migration <{migration_id}> {direction} executed on db <{self.db_name}>: .+)"
    return bool(re.search(search_pattern, self.get_file_text("history.txt")))
    
  def do_the_thing(self, migration_id=None, direction=""):
    if direction != "UPGRADE" and direction != "DOWNGRADE":
      print("<direction> must equal either 'UPGRADE' or 'DOWNGRADE'")
      return
    try:
      if not migration_id:
        migration_ledger_item = self.get_ledger_item(migration_id=None)
        migration_id = migration_ledger_item["id"]
      if self.migration_has_been_executed(migration_id, direction):
        answer = input(f"an {direction} on migration <{migration_id}> has previously been executed on database <{self.db_name}>. Do you wish to continue? [y/n]")
        if answer.lower() == "y":
          pass
        else:
          print("Aborting...")
          return
      script_module = self.get_migration_script_module(migration_id)
      if script_module:
        sql_text = script_module.upgrade() if direction == "UPGRADE" else script_module.downgrade()
        print(sql_text)
        answer = input(f"Do you wish to continue with the above migration on database <{self.db_name}>? [y/n]")
        if answer.lower() == "y":
          self.execute_sql(sql_text)
          self.write_history(f"migration <{migration_id}> {direction} executed on db <{self.db_name}>: {datetime.utcnow().isoformat()}\n")
          print(f"{direction} successful")
        else:
          print("Aborting...")
          return
      else:
        print(f"No script module found for migration_id <{migration_id}>")
    except BaseException as e:
      print(f"{direction} FAILED", e)

  def upgrade(self, migration_id=None):
    self.do_the_thing(migration_id, "UPGRADE")

  def downgrade(self, migration_id=None):
    self.do_the_thing(migration_id, "DOWNGRADE")