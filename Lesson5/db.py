import sqlite3

DB_NAME = "people.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS people (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL
        );
    """)
    conn.commit()
    conn.close()

def add_person(name, age):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO people (name, age) VALUES (?, ?)", (name, age))
    conn.commit()
    conn.close()

def get_all_people():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM people")
    rows = cursor.fetchall()
    conn.close()
    return rows
