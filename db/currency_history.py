from db.conn import cur


def insert_currency_history(name: str, value: float):
	cur.execute(
		"""
		INSERT INTO currency_history (name, value)
		VALUES (?, ?)
	""",
		(name, value),
	)
	cur.execute("COMMIT")


def update_currency_history(name: str, value: float):
	cur.execute(
		"""
		UPDATE currency_history
		SET value = ?
		WHERE name = ?
	""",
		(value, name),
	)
	cur.execute("COMMIT")


def get_currency_history(name: str):
	cur.execute(
		"""
		SELECT * FROM currency_history
		WHERE name = ?
	""",
		(name,),
	)
	return cur.fetchone()


def get_currency_histories():
	cur.execute("""
		SELECT * FROM currency_history
	""")
	return cur.fetchall()


def get_currency_history_by_date(name: str, date: str):
	cur.execute(
		"""
		SELECT * FROM currency_history
		WHERE name = ? AND date = ?
	""",
		(name, date),
	)
	return cur.fetchone()
