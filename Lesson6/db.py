import sqlite3

DB_NAME = "app.db"

def init_db():
    with sqlite3.connect(DB_NAME) as conn:
        cur = conn.cursor()

        cur.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                role TEXT DEFAULT 'user'
            )
        """)

        cur.execute("""
            CREATE TABLE IF NOT EXISTS person (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER
            )
        """)

        cur.execute("INSERT OR IGNORE INTO users (username, password, role) VALUES (?, ?, ?)", ("admin", "admin", "admin"))
        conn.commit()

def check_user(username, password):
    with sqlite3.connect(DB_NAME) as conn:
        cur = conn.cursor()
        cur.execute("SELECT role FROM users WHERE username=? AND password=?", (username, password))
        result = cur.fetchone()
        if result:
            return True, result[0]
        return False, None

def create_user(username, password, role="user"):
    if not username or not password:
        return False, "Логин и пароль не могут быть пустыми."

    with sqlite3.connect(DB_NAME) as conn:
        cur = conn.cursor()
        try:
            cur.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)", (username, password, role))
            conn.commit()
            return True, "Пользователь успешно создан."
        except sqlite3.IntegrityError:
            return False, "Пользователь с таким логином уже существует."

def get_all():
    with sqlite3.connect(DB_NAME) as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM person")
        return cur.fetchall()

def search_by_name(name):
    with sqlite3.connect(DB_NAME) as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM person WHERE name LIKE ?", ('%' + name + '%',))
        return cur.fetchall()

def delete_by_id(person_id):
    with sqlite3.connect(DB_NAME) as conn:
        cur = conn.cursor()
        cur.execute("DELETE FROM person WHERE id = ?", (person_id,))
        conn.commit()

def add_person(name, age):
    with sqlite3.connect(DB_NAME) as conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO person (name, age) VALUES (?, ?)", (name, age))
        conn.commit()
