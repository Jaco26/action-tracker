description = "This is my the database schema as it exists in version 1 of the app."
id = "9f7a20ded1af4e5da8a5d658e50611c4"
date_created = "2019-04-14T16:54:13.318511"

def upgrade():
  return """
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE TABLE IF NOT EXISTS revoked_token (
	id SERIAL PRIMARY KEY,
	jti VARCHAR
);

CREATE TABLE IF NOT EXISTS users (
	id UUID PRIMARY KEY default uuid_generate_v4(),
	role INT default 1,
	username VARCHAR UNIQUE NOT NULL,
	pw_hash VARCHAR UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS action_category (
	id UUID PRIMARY KEY default uuid_generate_v4(),
	user_id UUID references users(id) NOT NULL,
	category_name VARCHAR NOT NULL
);

CREATE TABLE IF NOT EXISTS action_taken (
	id UUID PRIMARY KEY default uuid_generate_v4(),
	user_id UUID references users(id),
	ts TIMESTAMPTZ DEFAULT timezone('utc', now()),
	duration TSTZRANGE,
	category_id UUID references action_category(id) NOT NULL,
	description VARCHAR
);
"""

def downgrade():
	return """
DROP EXTENSION "uuid-ossp";

DROP TABLE revoked_token;

DROP TABLE users;

DROP TABLE action_category;

DROP TABLE action_taken;
"""