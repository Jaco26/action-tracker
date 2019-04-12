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

  def create_migration(self, options):
    options.update({
      "id": uuid.uuid4().hex,
      "date_created": datetime.utcnow().isoformat(),
    })
    with open(f"{self.directory}/ledger.txt", "a") as ledger_f:
      ledger_f.write(options["id"] + "\n")

    with open(f"{self.directory}/template.txt", "r") as template_f:
      with open(f"{self.directory}/versions/{options['id']}.py", "w") as target_f:
        template_str = template_f.read()
        for key in options.keys():
          print(key, template_str)
          template_str = template_str.replace(f"%{key}%", options[key])
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
