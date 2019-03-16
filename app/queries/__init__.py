from app.db import pool

@pool.execute()
def drop_tables():
  return """
    DROP TABLE users CASCADE;
    DROP TABLE revoked_token;
    DROP TABLE action_category CASCADE;
    DROP TABLE action_taken;
  """

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
      action_name VARCHAR UNIQUE NOT NULL
    );

    CREATE TABLE IF NOT EXISTS action_taken 
    (
      user_id UUID references users(id),
      ts TIMESTAMPTZ DEFAULT timezone('utc'::text, now()),
      duration TSTZRANGE,
      category_id UUID references action_category(id) NOT NULL,
      description VARCHAR
    );
  """

@pool.execute()
def insert_user_and_action_category():
  return """
    INSERT INTO users (username, pw_hash) VALUES ('Jacob', 'asdfasdf');

    INSERT INTO action_category (action_name) VALUES ('took walk');
  """

@pool.execute()
def insert_test_values():
  return """
    INSERT INTO action_taken (user_id, duration, category_id, description) 
    VALUES (
      (SELECT id FROM users WHERE username ILIKE %s ESCAPE ''),
      '[2018-10-21 14:30, 2018-10-21 14:50]',
      (SELECT id FROM action_category WHERE action_name ILIKE %s ESCAPE ''),
      'I walked around to the river and back'
    );
  """, ('%jacob%', '%walk%')


