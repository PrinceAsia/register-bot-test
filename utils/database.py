import sqlite3

from aiogram.types import user


class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS users("
            "id TEXT UNIQUE PRIMARY KEY,"
            "username TEXT UNIQUE,"
            "first_name TEXT,"
            "last_name TEXT,"
            "phone_number TEXT UNIQUE,"
            "location TEXT,"
            "address TEXT)"
        )
        self.conn.commit()

    def add_user(self, user) -> bool:
        try:
            self.cursor.execute(
                "INSERT INTO users(id, username, first_name, last_name) VALUES (?, ?, ?, ?)",
                (user['id'], user['username'], user['first_name'], user['last_name'])
            )
            self.conn.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def has_user(self, user_id) -> bool:
        try:
            self.cursor.execute("SELECT id, first_name FROM users WHERE id = ?", (user_id,))
            return self.cursor.fetchone() is not None
        except Exception as e:
            print(e)
            return False

    def is_registered(self, user_id) -> bool:
        try:
            self.cursor.execute("SELECT registered FROM users WHERE id = ?", (user_id,))
            return self.cursor.fetchone()[0]
        except Exception as e:
            print(e)
            return False

    def update_any_col(self, user_id, cols, values) -> bool:
        print(cols)
        print(values)
        try:
            sql = "UPDATE users SET "
            for i in range(len(cols)):
                sql += cols[i] + "=?, "
            sql = sql[:-2]
            print(sql)
            sql += f" WHERE id = {user_id}"
            self.cursor.execute(sql, values)
            self.conn.commit()
            return True
        except Exception as e:
            print(e)
            return False
