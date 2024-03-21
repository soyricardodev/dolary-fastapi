from pydantic import BaseModel

from db.conn import cur


class Currency(BaseModel):
	id: int
	name: str
	origin: str
	country: str
	value: float
	updated_at: str


def insert_currency(name: str, value: float, origin: str, country: str):
	cur.execute(
		"""
		INSERT INTO currency (name, origin, country, value)
		VALUES (?, ?, ?, ?)
	""",
		(name, origin, country, value),
	)
	cur.execute("COMMIT")


def update_currency(name: str, value: float, origin: str, country: str):
	cur.execute(
		"""
		UPDATE currency
		SET value = ?
		WHERE name = ? AND origin = ? AND country = ?
	""",
		(value, name, origin, country),
	)
	cur.execute("COMMIT")


def get_currency(name: str, origin: str, country: str):
	cur.execute(
		"""
    SELECT * FROM currency
    WHERE name = ? AND origin = ? AND country = ?
  """,
		(name, origin, country),
	)
	currency = cur.fetchone()
	cols = [column[0] for column in cur.description]
	results = dict(zip(cols, currency))

	if currency:
		return Currency(**results)
	else:
		return None


def get_currencies():
	cur.execute("""
		SELECT * FROM currency
	""")
	currencies = cur.fetchall()
	cols = [column[0] for column in cur.description]
	results = [dict(zip(cols, currency)) for currency in currencies]

	return [Currency(**result) for result in results]
