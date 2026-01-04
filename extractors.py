from bs4 import BeautifulSoup
from urllib.parse import urljoin
from typing import Optional

def clean_text(text: str) -> str:
    return " ".join(text.split())

def extract_company_name(soup: BeautifulSoup) -> Optional[str]:
    og = soup.find("meta", property="og:site_name")
    if og and og.get("content"):
        return clean_text(og["content"])

    if soup.title and soup.title.text:
        title = clean_text(soup.title.text)
        for sep in ["|", "-", "–"]:
            if sep in title:
                title = title.split(sep)[0]
        return title
    return None

def extract_what_they_do(soup: BeautifulSoup) -> Optional[str]:
    meta = soup.find("meta", attrs={"name": "description"})
    if meta and meta.get("content"):
        return clean_text(meta["content"])

    for p in soup.find_all("p"):
        text = clean_text(p.get_text())
        if len(text) > 60:
            return text
    return None

def extract_offerings(soup: BeautifulSoup) -> list[str]:
    offerings = set()
    for li in soup.find_all("li"):
        text = clean_text(li.get_text())
        if 3 <= len(text.split()) <= 6:
            offerings.add(text)
    return list(offerings)

def extract_proof_signals(soup: BeautifulSoup) -> list[str]:
    keywords = ["trusted by", "used by", "serving", "customers", "award"]
    signals = []
    for t in soup.stripped_strings:
        for kw in keywords:
            if kw in t.lower() and len(t.split()) <= 15:
                signals.append(clean_text(t))
    return list(set(signals))

def find_link(soup, base_url, keywords):
    for a in soup.find_all("a", href=True):
        href = a["href"].lower()
        text = a.get_text(strip=True).lower()
        for kw in keywords:
            if kw in href or kw in text:
                return urljoin(base_url, a["href"])
    return None

def extract_contact_page(soup, base_url):
    return find_link(soup, base_url, ["contact", "get-in-touch"])

def extract_careers_page(soup, base_url):
    return find_link(soup, base_url, ["careers", "jobs"])
