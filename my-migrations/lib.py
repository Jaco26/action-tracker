import os
import uuid



@pool.execute()
def upgrade(sql):
  pass



def downgrade(sql):
  
  @pool.execute()
  def do_downgrade():
    return sql
  
  do_downgrade()

  



