import sqlite3

conn = sqlite3.connect('database.db')

cursor = conn.cursor()

# Alerts Table
cursor.execute('''
CREATE TABLE IF NOT EXISTS alerts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    location TEXT,
    emergency_type TEXT,
    message TEXT
)
''')

# Users Table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    email TEXT,
    password TEXT
)
''')

conn.commit()
conn.close()

print("Database Created Successfully!")