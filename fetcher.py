import requests
from bs4 import BeautifulSoup

def fetch_homepage(url: str) -> BeautifulSoup:
    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; CompanyScraper/1.0)"
    }
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()
    return BeautifulSoup(response.text, "lxml")
