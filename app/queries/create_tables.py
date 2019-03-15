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
      username VARCHAR,
      pw_hash VARCHAR
    );

    CREATE TABLE IF NOT EXISTS action_category 
    (
      id SERIAL PRIMARY KEY,
      action_name VARCHAR
    );

    CREATE TABLE IF NOT EXISTS action_taken 
    (
      user_id UUID references users(id),
      ts TIMESTAMPTZ DEFAULT timezone('utc'::text, now()),
      category INT references action_category(id),
      description VARCHAR
    );
  """