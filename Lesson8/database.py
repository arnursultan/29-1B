import sqlite3

DB_NAME = "hamster.db"

def init_db():
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS stats (
                id INTEGER PRIMARY KEY,
                score INTEGER DEFAULT 0,
                image_path TEXT DEFAULT '',
                label_text TEXT DEFAULT 'Ударов'
            )
        """)
        conn.execute("INSERT OR IGNORE INTO stats (id) VALUES (1)")
        conn.commit()

def get_data():
    with sqlite3.connect(DB_NAME) as conn:
        cur = conn.cursor()
        cur.execute("SELECT score, image_path, label_text FROM stats WHERE id = 1")
        return cur.fetchone()

def update_data(score=None, image_path=None, label_text=None):
    with sqlite3.connect(DB_NAME) as conn:
        if score is not None:
            conn.execute("UPDATE stats SET score = ? WHERE id = 1", (score,))
        if image_path is not None:
            conn.execute("UPDATE stats SET image_path = ? WHERE id = 1", (image_path,))
        if label_text is not None:
            conn.execute("UPDATE stats SET label_text = ? WHERE id = 1", (label_text,))
        conn.commit()

def reset_all():
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute("UPDATE stats SET score = 0, image_path = '', label_text = 'Ударов' WHERE id = 1")
        conn.commit()
