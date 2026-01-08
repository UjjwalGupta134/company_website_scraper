from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from fetcher import fetch_homepage
from extractors import *
from schemas import CompanyProfile, ScrapeRequest

app = FastAPI(title="Company Website Scraper")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
def home():
    with open("static/index.html", "r", encoding="utf-8") as f:
        return f.read()

@app.post("/scrape", response_model=CompanyProfile)
def scrape(req: ScrapeRequest):
    soup = fetch_homepage(req.website)
    return CompanyProfile(
        website=req.website,
        company_name=extract_company_name(soup),
        what_they_do=extract_what_they_do(soup),
        offerings=extract_offerings(soup),
        proof_signals=extract_proof_signals(soup),
        contact_page=extract_contact_page(soup, req.website),
        careers_page=extract_careers_page(soup, req.website),
    )

