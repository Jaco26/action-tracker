import os
from dotenv import load_dotenv
from datetime import datetime
from my_migrations.lib import Manager
from my_migrations.script_gen import ScriptGen

load_dotenv()

manager = Manager(os.environ.get("DATABASE_URL"))
script = ScriptGen()

