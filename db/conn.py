from sqlite3 import connect

conn = connect("currency.sqlite")
cur = conn.cursor()

cur.executescript("""
  CREATE TABLE IF NOT EXISTS currency (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    origin TEXT NOT NULL,
    country TEXT NOT NULL,
    value REAL NOT NULL,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
  );
""")

cur.executescript("""
  CREATE TABLE IF NOT EXISTS currency_history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    origin TEXT NOT NULL,
    country TEXT NOT NULL,
    value REAL NOT NULL,
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
  );
""")
