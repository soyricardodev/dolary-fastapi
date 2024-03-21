from re import findall

from bs4 import BeautifulSoup
from requests import get


def scrape_website(url: str, verify: bool = True) -> BeautifulSoup:
	response = get(url, verify=verify)
	soup = BeautifulSoup(response.content, "html.parser")
	return soup


regex_extract_numbers_and_comma = r"[\d,]+"


def extract_numbers_from_string(value: str) -> float:
	return float(findall(regex_extract_numbers_and_comma, value)[0].replace(",", "."))
