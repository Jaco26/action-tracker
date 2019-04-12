


class ScriptGen:
  def __init(self):
    self.up = [] # push upgrade statements here
    self.down = [] # push inverse, downgrade statements here

  # ALTER TABLE
  def alter_table(self, tablename):
    altr_tbl = f"ALTER TABLE {tablename}"

    # ADD COLUMN
    def add_col(colname, coltype, only_return=False):
      stmt = f"{altr_tbl} ADD COLUMN {colname} {coltype};"
      if not only_return and stmt not in self.up:
        self.up.push(stmt)
        self.down.push(drop_col(colname, True))
      return stmt

    # DROP COLUMN
    def drop_col(colname, only_return=False):
      stmt = f"{altr_tbl} DROP COLUMN {colname};"
      if not only_return and stmt not in self.up:
        self.up.push(stmt)
        self.down.push(add_col(colname, "<<DEFINITION NEEDED>>", True))
      return stmt

    # RENAME COLUMN
    def rename_col(colname, new_colname, only_return=False):
      stmt = f"{altr_tbl} RENAME COLUMN {colname} TO {new_colname};"
      if not only_return and stmt not in self.up:
        self.up.push(stmt)
        self.down.push(rename_col(new_colname, colname, True))
      return stmt

    # ALTER COLUMN
    def alter_col(colname):
      altr_clm = f"{altr_tbl} ALTER COLUMN {colname}"
      
      # SET DEFAULT
      def set_default(value, only_return=False):
        stmt = f"{altr_clm} SET DEFAULT {value};"
        if not only_return and stmt not in self.up:
          self.up.push(stmt)
          self.down.push(drop_default(True))
        return stmt
    
      # DROP DEFAULT
      def drop_default(only_return=False):
        stmt = f"{altr_clm} DROP DEFAULT;"
        if not only_return and stmt not in self.up:
          self.up.push(stmt)
          self.down.push(set_default("<<DEFINITION NEEDED>>", True))
        return stmt

      # SET NOT NULL
      def set_not_null(only_return=False):
        stmt = f"{altr_clm} SET NOT NULL;"
        if not only_return and stmt not in self.up:
          self.up.push(stmt)
          self.down.push(drop_not_null(True))
        return stmt

      # DROP NOT NULL
      def drop_not_null(only_return=False):
        stmt = f"{altr_clm} DROP NOT NULL;"
        if not only_return and stmt not in self.up:
          self.up.push(stmt)
          self.down.push(set_not_null(True))
        return stmt

      return dict(
        set_default=set_default,
        drop_default=drop_default,
        set_not_null=set_not_null,
        drop_not_null=drop_not_null,
      )

    # ADD CONSTRAINT
    def add_constraint(constraint_name, constraint_definition, only_return=False):
      stmt = f"{altr_tbl} ADD CONSTRAINT {constraint_name} {constraint_definition};"
      if not only_return and stmt not in self.up:
        self.up.push(stmt)
        self.down.push(drop_constraint(constraint_name, True))
      return stmt

    # DROP CONSTRAINT
    def drop_constraint(constraint_name, only_return=False):
      stmt = f"{altr_tbl} DROP CONSTRAINT {constraint_name};"
      if not only_return and stmt not in self.up:
        self.up.push(stmt)
        self.down.push(add_constraint(constraint_name, "<<DEFINITION NEEDED>>", True))
      return stmt

    # RENAME TO
    def rename_to(new_tablename, only_return=False):
      stmt = f"{altr_tbl} RENAME TO {new_tablename};"
      if not only_return and stmt not in self.up:
        self.up.push(stmt)
        self.down.push(rename_to(new_tablename, tablename, True))
      return stmt

    