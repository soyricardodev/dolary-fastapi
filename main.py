from fastapi import FastAPI

from cron.ve import save_data_in_db
from db.currency import get_currencies, get_currency

app = FastAPI()

save_data_in_db()


@app.get("/")
async def root():
	return get_currencies()


@app.get("/bcv")
async def bcv():
	return get_currency("usd", "bcv", "ve")


@app.get("/paralelo")
async def paralelo():
	return get_currency("usd", "paralelo", "ve")
