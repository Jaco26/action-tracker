import os
from datetime import datetime
from my_migrations.lib import Manager
from my_migrations.script_gen import ScriptGen

manager = Manager(os.environ.get("DATABASE_URL"))

script = ScriptGen()

script.create_extension_if_not_exists("uuid-ossp")
script.create_table_if_not_exists("revoked_token", False,
    "id SERIAL PRIMARY KEY,",
    "jti VARCHAR"
)
script.create_table_if_not_exists("users", False,
    "id UUID PRIMARY KEY default uuid_generate_v4(),",
    "role INT default 1,",
    "username VARCHAR UNIQUE NOT NULL,",
    "pw_hash VARCHAR UNIQUE NOT NULL"
)
script.create_table_if_not_exists("action_category", False,
    "id UUID PRIMARY KEY default uuid_generate_v4(),",
    "user_id UUID references users(id) NOT NULL,",
    "category_name VARCHAR NOT NULL"
)
script.create_table_if_not_exists("action_taken", False,
    "id UUID PRIMARY KEY default uuid_generate_v4(),",
    "user_id UUID references users(id),",
    "ts TIMESTAMPTZ DEFAULT timezone('utc', now()),",
    "duration TSTZRANGE,",
    "category_id UUID references action_category(id) NOT NULL,",
    "description VARCHAR"
)

if __name__ == "__main__":
    pass
#   manager.create_migration(
#       description="This is my the database schema as it exists in version 1 of the app.",
#       up_text="".join(script.up),
#       down_text="".join(script.down)
#   )

