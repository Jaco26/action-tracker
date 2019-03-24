from app.db import pool

@pool.execute()
def drop_tables():
  # return """
  #   DROP TABLE users CASCADE;
  #   DROP TABLE revoked_token;
  #   DROP TABLE action_category CASCADE;
  #   DROP TABLE action_taken;
  # """
  pass

@pool.execute()
def create_tables():
  return """
    CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

    CREATE TABLE IF NOT EXISTS revoked_token 
    (
      id SERIAL PRIMARY KEY,
      jti VARCHAR
    );

    CREATE TABLE IF NOT EXISTS users 
    (
      id UUID PRIMARY KEY default uuid_generate_v4(),
      role INT default 1,
      username VARCHAR UNIQUE NOT NULL,
      pw_hash VARCHAR UNIQUE NOT NULL
    );

    CREATE TABLE IF NOT EXISTS action_category
    (
      id UUID PRIMARY KEY default uuid_generate_v4(),
      user_id UUID references users(id) NOT NULL,
      category_name VARCHAR NOT NULL
    );

    CREATE TABLE IF NOT EXISTS action_taken 
    (
      id UUID PRIMARY KEY default uuid_generate_v4(),
      user_id UUID references users(id),
      ts TIMESTAMPTZ DEFAULT timezone('utc', now()),
      duration TSTZRANGE,
      category_id UUID references action_category(id) NOT NULL,
      description VARCHAR
    );
  """