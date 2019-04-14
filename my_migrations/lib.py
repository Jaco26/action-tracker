import os
import uuid
import psycopg2
import importlib
from datetime import datetime


class Manager:
  def __init__(self, db_uri):
    self.db_uri = db_uri
    self.directory = os.path.dirname(os.path.abspath(__file__))

  def execute_sql(self, sql):
    with psycopg2.connect(self.db_uri) as conn:
      with conn.cursor() as c:
        c.execute(sql)
    conn.close()

  def create_migration(self, description, up_text, down_text):
    meta = {
      "id": uuid.uuid4().hex,
      "date_created": datetime.utcnow().isoformat(),
    }

    with open(f"{self.directory}/ledger.txt", "a") as ledger_f:
      ledger_f.write("\n")
      ledger_f.write("-----" * 9 + "\n")
      ledger_f.write(f"id:          {meta['id']}\n")
      ledger_f.write(f"date:        {meta['date_created']}\n")
      ledger_f.write(f"description: {description}\n")
      ledger_f.write("-----" * 9 + "\n")

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



  def execute_migration(self, direction, migration_id=None):
    with open(f"{self.directory}/ledger.txt", "r") as ledger_f:
      if migration_id:
        module = importlib.import_module(f"my_migrations.versions.{migration_id}")
        print(module.upgrade().strip())
      else:
        lines = [line.replace("\n", "") for line in ledger_f]
        module = importlib.import_module(f"my_migrations.versions.{lines[-1]}")

        print(module.upgrade())
        # migration_file_path = f"{self.directory}/versions/{lines[-1]}.py"

  def downgrade(self, migration_name):
    pass