import sqlite3

class HilbertBasicDB:
    def __init__(self, db_file="hilbertbasic.db"):
        self.db_file = db_file
        self.conn = sqlite3.connect(self.db_file)
        self.cursor = self.conn.cursor()

    def create_table(self, table_name, columns: dict):
        cols = ', '.join([f"{col} {dtype}" for col, dtype in columns.items()])
        self.cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({cols})")
        self.conn.commit()

    def insert(self, table_name, data: dict):
        keys = ', '.join(data.keys())
        placeholders = ', '.join(['?'] * len(data))
        values = tuple(data.values())
        self.cursor.execute(f"INSERT INTO {table_name} ({keys}) VALUES ({placeholders})", values)
        self.conn.commit()

    def update(self, table_name, updates: dict, where_clause: str, where_params: tuple):
        set_clause = ', '.join([f"{k} = ?" for k in updates.keys()])
        values = tuple(updates.values()) + where_params
        self.cursor.execute(f"UPDATE {table_name} SET {set_clause} WHERE {where_clause}", values)
        self.conn.commit()

    def delete(self, table_name, where_clause: str, where_params: tuple):
        self.cursor.execute(f"DELETE FROM {table_name} WHERE {where_clause}", where_params)
        self.conn.commit()

    def query(self, sql, params=None):
        self.cursor.execute(sql, params or ())
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.conn.close()
