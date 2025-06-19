import sqlite3
import csv
import os

class SQLiteHelper:
    def __init__(self, db_file='database.db', auto_close=True):
        self.db_file = db_file
        self.auto_close = auto_close
        self.conn = None
        self.cursor = None
        self.connect()

    def connect(self):
        try:
            self.conn = sqlite3.connect(self.db_file)
            self.cursor = self.conn.cursor()
        except sqlite3.Error as e:
            raise ConnectionError(f"SQLite connection failed: {e}")

    def create_table(self, table_name, columns: dict):
        try:
            cols = ', '.join([f"{col} {dtype}" for col, dtype in columns.items()])
            self.cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({cols})")
            self.conn.commit()
        except sqlite3.Error as e:
            raise RuntimeError(f"Failed to create table '{table_name}': {e}")

    def insert_data(self, table_name, data: dict):
        try:
            keys = ', '.join(data.keys())
            placeholders = ', '.join(['?'] * len(data))
            values = tuple(data.values())
            self.cursor.execute(f"INSERT INTO {table_name} ({keys}) VALUES ({placeholders})", values)
            self.conn.commit()
        except sqlite3.Error as e:
            raise RuntimeError(f"Insert failed on table '{table_name}': {e}")

    def update_data(self, table_name, updates: dict, where: str, params: tuple):
        try:
            set_clause = ', '.join([f"{k} = ?" for k in updates.keys()])
            values = tuple(updates.values()) + params
            sql = f"UPDATE {table_name} SET {set_clause} WHERE {where}"
            self.cursor.execute(sql, values)
            self.conn.commit()
        except sqlite3.Error as e:
            raise RuntimeError(f"Update failed on table '{table_name}': {e}")

    def delete_data(self, table_name, where: str, params: tuple):
        try:
            sql = f"DELETE FROM {table_name} WHERE {where}"
            self.cursor.execute(sql, params)
            self.conn.commit()
        except sqlite3.Error as e:
            raise RuntimeError(f"Delete failed on table '{table_name}': {e}")

    def query(self, sql, params=None):
        try:
            self.cursor.execute(sql, params or ())
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            raise RuntimeError(f"Query failed: {e}")

    def describe_table(self, table_name):
        try:
            self.cursor.execute(f"PRAGMA table_info({table_name})")
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            raise RuntimeError(f"Failed to describe table '{table_name}': {e}")

    def list_tables(self):
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        return [tbl[0] for tbl in self.cursor.fetchall()]

    def export_to_csv(self, table_name, file_name):
        try:
            self.cursor.execute(f"SELECT * FROM {table_name}")
            rows = self.cursor.fetchall()
            headers = [i[0] for i in self.cursor.description]
            with open(file_name, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(headers)
                writer.writerows(rows)
        except Exception as e:
            raise RuntimeError(f"Export to CSV failed for '{table_name}': {e}")

    def help(self):
        return """
Available Methods:
- create_table(table_name, columns: dict)
- insert_data(table_name, data: dict)
- update_data(table_name, updates: dict, where: str, params: tuple)
- delete_data(table_name, where: str, params: tuple)
- query(sql, params=None)
- describe_table(table_name)
- list_tables()
- export_to_csv(table_name, filename)
- close()
        """

    def close(self):
        if self.conn:
            self.cursor.close()
            self.conn.close()

    def __del__(self):
        if self.auto_close:
            self.close()