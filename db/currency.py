from datetime import datetime

from pydantic import BaseModel

from db.conn import cur
from db.currency_history import insert_currency_history


class Currency(BaseModel):
	name: str
	origin: str
	country: str
	value: float
	date: float


def create_currency(name: str, origin: str, country: str):
	create_currency_query = cur.execute(
		"""
		INSERT INTO currency (name, origin, country)
		VALUES (?, ?, ?);
	""",
		(name, origin, country),
	)
	cur.execute("COMMIT")
	return create_currency_query.lastrowid


def insert_currency(name: str, value: float, origin: str, country: str):
	select_currency_query = cur.execute(
		"""
		SELECT
			c.id
		FROM currency AS c
		WHERE
			c.name = ?
			AND c.origin = ?
			AND c.country = ?
	""",
		(name, origin, country),
	)
	currency = select_currency_query.fetchone()

	now = datetime.now().timestamp()

	if currency is not None and currency[0] > 0:
		insert_currency_history(currency[0], value, now)
	else:
		new_currency = create_currency(name, origin, country)

		if new_currency is not None and new_currency > 0:
			insert_currency_history(new_currency, value, now)


def get_currency(currency_id: int):
	cur.execute(
		"""
		SELECT
			c.name,
			c.origin,
			c.country,
			ch.value,
			ch.date FROM currency AS c INNER JOIN currency_history AS ch ON c.id = ?
		""",
		(currency_id,),
	)

	currency = cur.fetchone()
	cols = [column[0] for column in cur.description]
	results = dict(zip(cols, currency))

	if currency:
		return Currency(**results)
	else:
		return None


def get_currencies_latest_values():
	cur.execute("""
		SELECT c.name, c.origin, c.country, ch.value, ch.date FROM currency AS c
		INNER JOIN currency_history AS ch ON c.id = ch.currency_id
		INNER JOIN
		(
		SELECT currency_id, MAX(date) AS max_date FROM currency_history GROUP BY currency_id
		) AS latest_dates ON ch.currency_id = latest_dates.currency_id AND ch.date
		= latest_dates.max_date;
	""")
	currencies = cur.fetchall()

	return [
		Currency(name=row[0], origin=row[1], country=row[2], value=row[3], date=row[4])
		for row in currencies
	]


def get_currencies_latest_value_by_name(name: str):
	cur.execute(
		"""
		SELECT c.name, c.origin, c.country, ch.value, ch.date FROM currency AS c
		INNER JOIN currency_history AS ch ON c.id = ch.currency_id
		INNER JOIN
		(
		SELECT currency_id, MAX(date) AS max_date FROM currency_history GROUP BY currency_id
		) AS latest_dates ON ch.currency_id = latest_dates.currency_id AND ch.date
		= latest_dates.max_date
		WHERE c.name = ?
	""",
		(name,),
	)

	currency = cur.fetchall()

	if currency:
		return [
			Currency(name=row[0], origin=row[1], country=row[2], value=row[3], date=row[4])
			for row in currency
		]
	else:
		return None


def get_currencies_latest_value_by_origin(origin: str):
	cur.execute(
		"""
		SELECT c.name, c.origin, c.country, ch.value, ch.date FROM currency AS c
		INNER JOIN currency_history AS ch ON c.id = ch.currency_id
		INNER JOIN
		(
		SELECT currency_id, MAX(date) AS max_date FROM currency_history GROUP BY currency_id
		) AS latest_dates ON ch.currency_id = latest_dates.currency_id AND ch.date
		= latest_dates.max_date
		WHERE c.origin = ?
	""",
		(origin,),
	)

	currency = cur.fetchall()

	if currency:
		return [
			Currency(name=row[0], origin=row[1], country=row[2], value=row[3], date=row[4])
			for row in currency
		]
	else:
		return None


def get_currencies_latest_value_by_country(country: str):
	currency = cur.execute(
		"""
		SELECT c.name, c.origin, c.country, ch.value, ch.date FROM currency AS c
		INNER JOIN currency_history AS ch ON c.id = ch.currency_id
		INNER JOIN
		(
		SELECT currency_id, MAX(date) AS max_date FROM currency_history GROUP BY currency_id
		) AS latest_dates ON ch.currency_id = latest_dates.currency_id AND ch.date
		= latest_dates.max_date
		WHERE c.country = ?
	""",
		(country,),
	)

	if currency:
		return Currency(**currency.fetchone())
	else:
		return None


def get_currency_latest_value_by_origin(name: str, origin: str):
	cur.execute(
		"""
		SELECT c.name, c.origin, c.country, ch.value, ch.date FROM currency AS c
		INNER JOIN currency_history AS ch ON c.id = ch.currency_id
		INNER JOIN
		(
		SELECT currency_id, MAX(date) AS max_date FROM currency_history GROUP BY currency_id
		) AS latest_dates ON ch.currency_id = latest_dates.currency_id AND ch.date
		= latest_dates.max_date
		WHERE c.name = ? AND c.origin = ?
	""",
		(name, origin),
	)

	currency = cur.fetchone()

	if currency:
		return Currency(
			name=currency[0], origin=currency[1], country=currency[2], value=currency[3], date=currency[4]
		)
	else:
		return None


def get_currency_by_day(currency_id: int, date_from: str, date_to: str):
	cur.execute(
		"""
		SELECT
			c.name,
			c.origin,
			c.country,
			ch.value,
			ch.date
		FROM currency AS c
		INNER JOIN currency_history AS ch ON c.id = ?
		WHERE ch.date BETWEEN ? AND ?
		""",
		(currency_id, date_from, date_to),
	)


def get_currency_updated_values_by_origin(name: str, origin: str):
	cur.execute(
		"""
		SELECT
			c.name,
			c.origin,
			c.country,
			ch.value,
			ch.date
		FROM currency AS c
		INNER JOIN currency_history AS ch ON c.name = ? AND c.origin = ?
		INNER JOIN (
			SELECT currency_id, MAX(date) AS max_date FROM currency_history GROUP BY currency_id
		) AS latest_dates ON ch.currency_id = latest_dates.currency_id
		AND ch.date = latest_dates.max_date;
	""",
		(
			name,
			origin,
		),
	)


def get_currency_updated_values_by_name(name: str):
	cur.execute(
		"""
		SELECT
			c.name,
			c.origin,
			c.country,
			ch.value,
			ch.date
		FROM currency AS c
		INNER JOIN currency_history AS ch ON c.name = ?
		INNER JOIN (
			SELECT currency_id, MAX(date) AS max_date FROM currency_history GROUP BY currency_id
		) AS latest_dates ON ch.currency_id = latest_dates.currency_id
		AND ch.date = latest_dates.max_date;
	""",
		(name,),
	)
