from collections import namedtuple

class ScriptGen:
  def __init__(self):
    self.up = [] # append upgrade statements here
    self.down = [] # append inverse, downgrade statements here

  # ALTER TABLE
  def alter_table(self, tablename):
    altr_tbl = f"ALTER TABLE {tablename}"

    # ADD COLUMN
    def add_col(colname, coltype, only_return=False):
      stmt = f"{altr_tbl} ADD COLUMN {colname} {coltype};"
      if not only_return and stmt not in self.up:
        self.up.append(stmt)
        self.down.append(drop_col(colname, True))
      return stmt

    # DROP COLUMN
    def drop_col(colname, only_return=False):
      stmt = f"{altr_tbl} DROP COLUMN {colname};"
      if not only_return and stmt not in self.up:
        self.up.append(stmt)
        self.down.append(add_col(colname, "<<DEFINITION NEEDED>>", True))
      return stmt

    # RENAME COLUMN
    def rename_col(colname, new_colname, only_return=False):
      stmt = f"{altr_tbl} RENAME COLUMN {colname} TO {new_colname};"
      if not only_return and stmt not in self.up:
        self.up.append(stmt)
        self.down.append(rename_col(new_colname, colname, True))
      return stmt

    # ALTER COLUMN
    def alter_col(colname):
      altr_clm = f"{altr_tbl} ALTER COLUMN {colname}"
      
      # SET DEFAULT
      def set_default(value, only_return=False):
        stmt = f"{altr_clm} SET DEFAULT {value};"
        if not only_return and stmt not in self.up:
          self.up.append(stmt)
          self.down.append(drop_default(True))
        return stmt
    
      # DROP DEFAULT
      def drop_default(only_return=False):
        stmt = f"{altr_clm} DROP DEFAULT;"
        if not only_return and stmt not in self.up:
          self.up.append(stmt)
          self.down.append(set_default("<<DEFINITION NEEDED>>", True))
        return stmt

      # SET NOT NULL
      def set_not_null(only_return=False):
        stmt = f"{altr_clm} SET NOT NULL;"
        if not only_return and stmt not in self.up:
          self.up.append(stmt)
          self.down.append(drop_not_null(True))
        return stmt

      # DROP NOT NULL
      def drop_not_null(only_return=False):
        stmt = f"{altr_clm} DROP NOT NULL;"
        if not only_return and stmt not in self.up:
          self.up.append(stmt)
          self.down.append(set_not_null(True))
        return stmt

      returnval = namedtuple("AlterMods", "set_default drop_default set_not_null drop_not_null")

      return returnval(
        set_default,
        drop_default,
        set_not_null,
        drop_not_null,
      )

    # ADD CONSTRAINT
    def add_constraint(constraint_name, constraint_definition, only_return=False):
      stmt = f"{altr_tbl} ADD CONSTRAINT {constraint_name} {constraint_definition};"
      if not only_return and stmt not in self.up:
        self.up.append(stmt)
        self.down.append(drop_constraint(constraint_name, True))
      return stmt

    # DROP CONSTRAINT
    def drop_constraint(constraint_name, only_return=False):
      stmt = f"{altr_tbl} DROP CONSTRAINT {constraint_name};"
      if not only_return and stmt not in self.up:
        self.up.append(stmt)
        self.down.append(add_constraint(constraint_name, "<<DEFINITION NEEDED>>", True))
      return stmt

    # RENAME TO
    def rename_to(new_tablename, only_return=False):
      stmt = f"{altr_tbl} RENAME TO {new_tablename};"
      if not only_return and stmt not in self.up:
        self.up.append(stmt)
        self.down.append(rename_to(new_tablename, tablename, True))
      return stmt

    returnval = namedtuple("AlterMods", "add_col drop_col rename_col alter_col add_constraint drop_constraint rename_to")
  
    return returnval(
      add_col,
      drop_col,
      rename_col,
      alter_col,
      add_constraint,
      drop_constraint,
      rename_to
    )