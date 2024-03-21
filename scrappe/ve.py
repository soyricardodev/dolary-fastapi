from typing import Any, Dict

from scrappe.lib import extract_numbers_from_string, scrape_website

bcv: Dict[str, Any] = {
	"origin": "bcv",
	"url": "https://bcv.org.ve",
	"sources": [
		{"name": "usd", "selector": "#dolar > div > div > div.col-sm-6.col-xs-6.centrado > strong"},
		{"name": "eur", "selector": "#euro > div > div > div.col-sm-6.col-xs-6.centrado > strong"},
		{"name": "yuan", "selector": "#yuan > div > div > div.col-sm-6.col-xs-6.centrado > strong"},
		{"name": "lira", "selector": "#lira > div > div > div.col-sm-6.col-xs-6.centrado > strong"},
		{"name": "rublo", "selector": "#rublo > div > div > div.col-sm-6.col-xs-6.centrado > strong"},
	],
}


def get_bcv_data():
	bcv_soup = scrape_website(bcv["url"], verify=False)
	bcv_usd = bcv_soup.select(bcv["sources"][0]["selector"])
	bcv_eur = bcv_soup.select(bcv["sources"][1]["selector"])
	bcv_yuan = bcv_soup.select(bcv["sources"][2]["selector"])
	bcv_lira = bcv_soup.select(bcv["sources"][3]["selector"])
	bcv_rublo = bcv_soup.select(bcv["sources"][4]["selector"])

	bcv_data = {
		"usd": extract_numbers_from_string(bcv_usd[0].text),
		"eur": extract_numbers_from_string(bcv_eur[0].text),
		"yuan": extract_numbers_from_string(bcv_yuan[0].text),
		"lira": extract_numbers_from_string(bcv_lira[0].text),
		"rublo": extract_numbers_from_string(bcv_rublo[0].text),
	}

	return bcv_data


paralelo: Dict[str, Any] = {
	"name": "paralelo",
	"url": "https://exchangemonitor.net/estadisticas/ve/dolar-enparalelovzla",
	"sources": [
		{
			"name": "usd",
			"selector": "body > section > div > div.row.inicio > div.col.texto > h2",
		}
	],
}


def get_paralelo_data():
	paralelo_soup = scrape_website(paralelo["url"])
	dolar_paralelo = paralelo_soup.select(paralelo["sources"][0]["selector"])
	dolar_value = extract_numbers_from_string(dolar_paralelo[0].text)
	return {"usd": dolar_value}
