import os
from datetime import datetime
from my_migrations.lib import Manager
from my_migrations.script_gen import ScriptGen

manager = Manager(os.environ.get("DATABASE_URL"))

script = ScriptGen()

script.alter_table("hello").add_col("greet", "VARCHAR")
script.alter_table("hello").drop_col("why")
script.create_table_if_not_exists("testytest", False,
    "id SERIAL PRIMARY KEY,",
    "name VARCHAR NOT NULL,",
    "age INTEGER"
)


if __name__ == "__main__":
    print(script.up)
    print(script.down)
#   manager.create_migration({
#     "version_name": "Jacob's version",
#     "upgrade_text": up,
#     "downgrade_text": down,
#   })
#   manager.execute_migration("up")