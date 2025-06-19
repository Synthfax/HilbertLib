import mysql.connector
from mysql.connector import Error
import csv

class MySQLHelper:
    def __init__(self, host='localhost', user='root', password='', database=None, auto_close=True):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.conn = None
        self.cursor = None
        self.auto_close = auto_close
        self.connect()

    def connect(self):
        try:
            self.conn = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            self.cursor = self.conn.cursor()
        except Error as e:
            raise ConnectionError(f"MySQL connection failed: {e}")

    def create_database(self, db_name):
        try:
            self.cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
        except Error as e:
            raise RuntimeError(f"Failed to create database '{db_name}': {e}")

    def use_database(self, db_name):
        try:
            self.cursor.execute(f"USE {db_name}")
        except Error as e:
            raise RuntimeError(f"Failed to switch to database '{db_name}': {e}")

    def list_databases(self):
        self.cursor.execute("SHOW DATABASES")
        return [db[0] for db in self.cursor.fetchall()]

    def list_tables(self):
        self.cursor.execute("SHOW TABLES")
        return [tbl[0] for tbl in self.cursor.fetchall()]

    def describe_table(self, table_name):
        self.cursor.execute(f"DESCRIBE {table_name}")
        return self.cursor.fetchall()

    def create_table(self, table_name, columns: dict):
        try:
            cols = ', '.join([f"{col} {dtype}" for col, dtype in columns.items()])
            self.cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({cols})")
        except Error as e:
            raise RuntimeError(f"Failed to create table '{table_name}': {e}")

    def insert_data(self, table_name, data: dict):
        try:
            keys = ', '.join(data.keys())
            vals = ', '.join(['%s'] * len(data))
            values = tuple(data.values())
            self.cursor.execute(f"INSERT INTO {table_name} ({keys}) VALUES ({vals})", values)
            self.conn.commit()
        except Error as e:
            raise RuntimeError(f"Insert failed on table '{table_name}': {e}")

    def update_data(self, table_name, updates: dict, where: str, params: tuple):
        try:
            set_clause = ', '.join([f"{k} = %s" for k in updates.keys()])
            values = tuple(updates.values()) + params
            sql = f"UPDATE {table_name} SET {set_clause} WHERE {where}"
            self.cursor.execute(sql, values)
            self.conn.commit()
        except Error as e:
            raise RuntimeError(f"Update failed on table '{table_name}': {e}")

    def delete_data(self, table_name, where: str, params: tuple):
        try:
            sql = f"DELETE FROM {table_name} WHERE {where}"
            self.cursor.execute(sql, params)
            self.conn.commit()
        except Error as e:
            raise RuntimeError(f"Delete failed on table '{table_name}': {e}")

    def search_by_column(self, table_name, column, value):
        try:
            self.cursor.execute(f"SELECT * FROM {table_name} WHERE {column} = %s", (value,))
            return self.cursor.fetchall()
        except Error as e:
            raise RuntimeError(f"Search failed on column '{column}' in '{table_name}': {e}")

    def query(self, sql, params=None):
        try:
            self.cursor.execute(sql, params or ())
            return self.cursor.fetchall()
        except Error as e:
            raise RuntimeError(f"Query failed: {e}")

    def export_to_csv(self, table_name, file_name):
        try:
            self.cursor.execute(f"SELECT * FROM {table_name}")
            rows = self.cursor.fetchall()
            headers = [i[0] for i in self.cursor.description]
            with open(file_name, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(headers)
                writer.writerows(rows)
        except Error as e:
            raise RuntimeError(f"Export to CSV failed for '{table_name}': {e}")
        except IOError as e:
            raise IOError(f"Failed to write CSV file '{file_name}': {e}")

    def help(self):
        return """
Available Methods:
- create_database(db_name)
- use_database(db_name)
- list_databases()
- list_tables()
- describe_table(table_name)
- create_table(table_name, columns: dict)
- insert_data(table_name, data: dict)
- update_data(table_name, updates: dict, where: str, params: tuple)
- delete_data(table_name, where: str, params: tuple)
- search_by_column(table_name, column, value)
- query(sql, params=None)
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
