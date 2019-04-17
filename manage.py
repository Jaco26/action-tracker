import os
from dotenv import load_dotenv
from datetime import datetime
from my_migrations.lib import Manager
from my_migrations.script_gen import ScriptGen

load_dotenv()

manager = Manager(os.environ.get("DATABASE_URL"))


if __name__ == "__main__":
    # manager.create_migration(
    #     description="This is just a testy westy.",
    #     up_text="".join(script.up),
    #     down_text="".join(script.down)
    # )

