description = "in 'action_taken', add column 'ts_override' to capture if users save an entry some time after they did an action and want to capture the time of action"
id = "68a8ba16b0b548d0a3027309747810bc"
date_created = "2019-04-18T00:58:04.563264"

def upgrade():
  return """
ALTER TABLE action_taken ADD COLUMN ts_override TIMESTAMPTZ;
"""

def downgrade():
  return """
ALTER TABLE action_taken DROP COLUMN ts_override;
"""