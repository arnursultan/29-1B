# import sqlite3
#
# connection = sqlite3.connect("test.db")
# cursor = connection.cursor()
#
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS users (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NOT NULL,
#     age INTEGER,
#     email TEXT UNIQUE
# )
# """)
#
# users = [
#     ("Artur", "20", "moldar@icloud.com"),
#     ("Daniel", "21", "rtdan04@yandex.by"),
#     ("Emily", "18", "emildily@icloud.com")
# ]
#
# cursor.executemany("INSERT INTO users (name, age, email) VALUES (?, ?, ?)", users)
#
# cursor.execute("SELECT * FROM users")
# rows = cursor.fetchall()
#
# print("Список пользователей:")
# for row in rows:
#     print(row)
#
# connection.commit()
# connection.close()

import sqlite3

connection = sqlite3.connect("database.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    email TEXT UNIQUE
)
""")

users = [
    ("Artur", 20, "artur.01@example.com"),
    ("Daniel", 21, "daniel.21@example.com"),
    ("Emily", 18, "emily_18@example.com"),
    ("Altynai", 22, "altynai22@example.com"),
    ("Alex", 24, "alex_24@example.com"),
    ("Alexey", 23, "alexey23@example.com"),
    ("Mukhammadali", 25, "mukhammadali25@example.com"),
    ("Aitolkun", 19, "aitolkun19@example.com"),
    ("Aidai", 20, "aidai20@example.com"),
    ("Alikhan", 21, "alikhan21@example.com"),
    ("Nurislam", 26, "nurislam26@example.com"),
    ("Zhanara", 22, "zhanara22@example.com"),
    ("Bakai", 27, "bakai27@example.com"),
    ("Adakhan", 18, "eliza18@example.com"),
    ("Danis", 23, "timur23@example.com")
]

cursor.executemany("INSERT OR IGNORE INTO users (name, age, email) VALUES (?, ?, ?)", users)
connection.commit()

min_age = int(input("Введите минимальный возраст: "))

cursor.execute("""
SELECT id, name, age, email
FROM users
WHERE age >= ?
ORDER BY id ASC
""", (min_age,))

results = cursor.fetchall()

if results:
    print(f"\nПользователи старше {min_age} лет:")
    for user in results:
        print(f"ID: {user[0]}, Имя: {user[1]}, Возраст: {user[2]}, Email: {user[3]}")
else:
    print("Пользователей по заданным критериям не найдено")

connection.close()