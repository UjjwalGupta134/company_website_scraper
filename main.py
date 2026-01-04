from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from fetcher import fetch_homepage
from extractors import *
from schemas import CompanyProfile

app = FastAPI(title="Company Website Scraper")
app.mount("/static", StaticFiles(directory="static"), name="static")

class ScrapeRequest(BaseModel):
    url: str

@app.get("/", response_class=HTMLResponse)
def home():
    with open("static/index.html", "r", encoding="utf-8") as f:
        return f.read()

@app.post("/scrape", response_model=CompanyProfile)
def scrape(req: ScrapeRequest):
    soup = fetch_homepage(req.url)
    return CompanyProfile(
        website=req.url,
        company_name=extract_company_name(soup),
        what_they_do=extract_what_they_do(soup),
        offerings=extract_offerings(soup),
        proof_signals=extract_proof_signals(soup),
        contact_page=extract_contact_page(soup, req.url),
        careers_page=extract_careers_page(soup, req.url),
    )
