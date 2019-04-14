from collections import namedtuple

class ScriptGen:
  def __init__(self):
    self.up = [] # append upgrade statements here
    self.down = [] # append inverse, downgrade statements here

  # CREATE TABLE IF NOT EXISTS
  def create_table_if_not_exists(self, tablename, only_return=False, *rows):
    stmt = f"\nCREATE TABLE IF NOT EXISTS {tablename} (\n"
    for row in rows:
      stmt += "\t" + row + "\n"
    stmt += ");\n"
    if not only_return and stmt not in self.up:
      self.up.append(stmt)
      self.down.append(self.drop_table(tablename, True))
    return stmt

  # DROP TABLE
  def drop_table(self, tablename, only_return=False):
    stmt = f"\nDROP TABLE {tablename};\n"
    if not only_return and stmt not in self.up:
      self.up.append(stmt)
      self.down.append(self.create_table_if_not_exists(tablename, True, "<<DEFINITION NEEDED>>"))
    return stmt
  
  # CREATE EXTENSION IF NOT EXISTS
  def create_extension_if_not_exists(self, extension_name, only_return=False):
    stmt = f"\nCREATE EXTENSION IF NOT EXISTS \"{extension_name}\";\n"
    if not only_return and stmt not in self.up:
      self.up.append(stmt)
      self.down.append(self.drop_extension(extension_name, True))
    return stmt

  # DROP EXTENSION
  def drop_extension(self, extension_name, only_return=False):
    stmt = f"\nDROP EXTENSION \"{extension_name}\";\n"
    if not only_return and stmt not in self.up:
      self.up.append(stmt)
      self.down.append(self.create_extension_if_not_exists(extension_name, True))
    return stmt

  # ALTER TABLE
  def alter_table(self, tablename):
    altr_tbl = f"\nALTER TABLE {tablename}"

    # ADD COLUMN
    def add_col(colname, coltype, only_return=False):
      stmt = f"{altr_tbl} ADD COLUMN {colname} {coltype};\n"
      if not only_return and stmt not in self.up:
        self.up.append(stmt)
        self.down.append(drop_col(colname, True))
      return stmt

    # DROP COLUMN
    def drop_col(colname, only_return=False):
      stmt = f"{altr_tbl} DROP COLUMN {colname};\n"
      if not only_return and stmt not in self.up:
        self.up.append(stmt)
        self.down.append(add_col(colname, "<<DEFINITION NEEDED>>", True))
      return stmt

    # RENAME COLUMN
    def rename_col(colname, new_colname, only_return=False):
      stmt = f"{altr_tbl} RENAME COLUMN {colname} TO {new_colname};\n"
      if not only_return and stmt not in self.up:
        self.up.append(stmt)
        self.down.append(rename_col(new_colname, colname, True))
      return stmt

    # ALTER COLUMN
    def alter_col(colname):
      altr_clm = f"{altr_tbl} ALTER COLUMN {colname}"
      
      # SET DEFAULT
      def set_default(value, only_return=False):
        stmt = f"{altr_clm} SET DEFAULT {value};\n"
        if not only_return and stmt not in self.up:
          self.up.append(stmt)
          self.down.append(drop_default(True))
        return stmt
    
      # DROP DEFAULT
      def drop_default(only_return=False):
        stmt = f"{altr_clm} DROP DEFAULT;\n"
        if not only_return and stmt not in self.up:
          self.up.append(stmt)
          self.down.append(set_default("<<DEFINITION NEEDED>>", True))
        return stmt

      # SET NOT NULL
      def set_not_null(only_return=False):
        stmt = f"{altr_clm} SET NOT NULL;\n"
        if not only_return and stmt not in self.up:
          self.up.append(stmt)
          self.down.append(drop_not_null(True))
        return stmt

      # DROP NOT NULL
      def drop_not_null(only_return=False):
        stmt = f"{altr_clm} DROP NOT NULL;\n"
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
      stmt = f"{altr_tbl} ADD CONSTRAINT {constraint_name} {constraint_definition};\n"
      if not only_return and stmt not in self.up:
        self.up.append(stmt)
        self.down.append(drop_constraint(constraint_name, True))
      return stmt

    # DROP CONSTRAINT
    def drop_constraint(constraint_name, only_return=False):
      stmt = f"{altr_tbl} DROP CONSTRAINT {constraint_name};\n"
      if not only_return and stmt not in self.up:
        self.up.append(stmt)
        self.down.append(add_constraint(constraint_name, "<<DEFINITION NEEDED>>", True))
      return stmt

    # RENAME TO
    def rename_to(new_tablename, only_return=False):
      stmt = f"{altr_tbl} RENAME TO {new_tablename};\n"
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