from sqlite3 import connect

conn = connect("currency.sqlite")
cur = conn.cursor()

cur.executescript("""
  CREATE TABLE IF NOT EXISTS currency (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    origin TEXT NOT NULL,
    country TEXT NOT NULL
  );
""")

cur.executescript("""
  CREATE TABLE IF NOT EXISTS currency_history (
    currency_id INTEGER NOT NULL,
    value REAL NOT NULL,
    date INTEGER NOT NULL
  );
""")

# INSERT INTO currency VALUES (1, 'USD', 'BCV', 'VE');
# INSERT INTO currency VALUES (2, 'EUR', 'BCV', 'VE');
# INSERT INTO currency VALUES (3, 'USD', 'Paralelo', 'VE');
#
#
# INSERT INTO currency_history VALUES (1, 38.40, '2024-03-21 23:04:00');
# INSERT INTO currency_history VALUES (3, 39.40, '2024-03-21 23:04:00');
#
# --Seleccionar todo
# SELECT c.name, c.origin, c.country, ch.value, ch.date FROM currency AS c
#  INNER JOIN currency_history AS ch ON c.id = ch.currency_id
#
# --Seleccionar todo por dia
# SELECT c.name, c.origin, c.country, ch.value, ch.date FROM currency AS c
# INNER JOIN currency_history AS ch ON c.id = ch.currency_id
# WHERE ch.date BETWEEN '2024-03-21 00:00:00' AND '2024-03-21 23:59:00'
# Algo así bro
# Y esta sería la consulta optimizada
# SELECT c.name, c.origin, c.country, ch.value, ch.date FROM currency AS c
# INNER JOIN currency_history AS ch ON c.id = ch.currency_id
# INNER JOIN
# (
# SELECT currency_id, MAX(date) AS max_date FROM currency_history GROUP BY currency_id
# ) AS latest_dates ON ch.currency_id = latest_dates.currency_id AND ch.date
# = latest_dates.max_date;
