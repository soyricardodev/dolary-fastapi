from db.currency import insert_currency
from scrappe.ve import get_bcv_data, get_paralelo_data


def save_data_in_db():
	bcv_data = get_bcv_data()
	paralelo_data = get_paralelo_data()

	for currency in bcv_data:
		insert_currency(currency, bcv_data[currency], "bcv", "ve")

	for currency in paralelo_data:
		insert_currency(currency, paralelo_data[currency], "paralelo", "ve")
