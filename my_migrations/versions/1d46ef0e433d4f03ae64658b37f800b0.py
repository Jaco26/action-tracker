description = "This is just a testy westy."
id = "1d46ef0e433d4f03ae64658b37f800b0"
date_created = "2019-04-14T18:38:27.586698"

def upgrade():
  return """
CREATE TABLE IF NOT EXISTS testywesty (
	id SERIAL PRIMARY KEY,
	name VARCHAR
);
"""

def downgrade():
  return """
DROP TABLE testywesty;
"""