import os
from datetime import datetime
from my_migrations.lib import Manager
from my_migrations.script_gen import ScriptGen

manager = Manager(os.environ.get("DATABASE_URL"))

script = ScriptGen()

script.create_table_if_not_exists("testywesty", False,
    "id SERIAL PRIMARY KEY,",
    "name VARCHAR"
)

if __name__ == "__main__":
    manager.create_migration(
        description="This is just a testy westy.",
        up_text="".join(script.up),
        down_text="".join(script.down)
    )

