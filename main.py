from fastapi import FastAPI

from db.currency import (
	get_currencies_latest_value_by_name,
	get_currency_latest_value_by_origin,
)

app = FastAPI()


# @app.get("/")
# async def root():
# 	return get_currencies_latest_values()


@app.get("/api/currency/{currency}")
async def get_currency(currency: str, origin: str | None = None):
	if origin:
		return get_currency_latest_value_by_origin(currency, origin)
	else:
		return get_currencies_latest_value_by_name(currency)
