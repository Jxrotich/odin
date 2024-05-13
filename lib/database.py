import sqlite3

class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def create_table(self, table_name, fields):
        query = f"CREATE TABLE IF NOT EXISTS {table_name} ({fields})"
        self.cursor.execute(query)
        self.conn.commit()

    def insert(self, table_name, data):
        columns = ', '.join(data.keys())
        placeholders = ', '.join(['?' for _ in range(len(data))])
        values = tuple(data.values())
        query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
        self.cursor.execute(query, values)
        self.conn.commit()

    def delete(self, table_name, condition):
        query = f"DELETE FROM {table_name} WHERE {condition}"
        self.cursor.execute(query)
        self.conn.commit()

    def update(self, table_name, data, condition):
        set_clause = ', '.join([f"{field} = ?" for field in data.keys()])
        query = f"UPDATE {table_name} SET {set_clause} WHERE {condition}"
        self.cursor.execute(query, list(data.values()))
        self.conn.commit()

    def select(self, table_name, condition=None):
        query = f"SELECT * FROM {table_name}"
        if condition is not None:
            query += f" WHERE {condition}"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def close(self):
        self.conn.close()
