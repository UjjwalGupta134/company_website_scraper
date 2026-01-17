import requests
from bs4 import BeautifulSoup

def is_blocked_page(html: str) -> bool:
    block_signatures = [
        "cf-challenge",
        "cloudflare",
        "attention required",
        "captcha",
        "verify you are human"
    ]
    html_lower = html.lower()
    return any(sig in html_lower for sig in block_signatures)


HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9",
}

def fetch_homepage(url: str) ->BeautifulSoup:
    response = requests.get(url, headers=headers, timeout=10)
response.raise_for_status()

html = response.text

if is_blocked_page(html):
    raise ValueError("BLOCKED_WEBSITE")

soup = BeautifulSoup(html, "html.parser")
return soup



