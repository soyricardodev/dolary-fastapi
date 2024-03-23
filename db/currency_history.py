from db.conn import cur


def insert_currency_history(currency_id: int, value: float, date: float):
	cur.execute(
		"""
			INSERT INTO currency_history (currency_id, value, date)
			VALUES (?, ?, ?);
		""",
		(currency_id, value, date),
	)
	cur.execute("COMMIT")


def get_currency_history(currency_id: int):
	cur.execute(
		"""
		SELECT * FROM currency_history
		WHERE currency_id = ?
	""",
		(currency_id,),
	)
	return cur.fetchall()
