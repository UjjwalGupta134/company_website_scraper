import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9",
}

def fetch_homepage(url: str):
    response = requests.get(
        url,
        headers=HEADERS,
        timeout=15,
        allow_redirects=True
    )
    response.raise_for_status()
    return BeautifulSoup(response.text, "html.parser")
