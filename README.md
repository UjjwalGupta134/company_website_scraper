# Company Website Scraper

## Overview
This project is a lightweight, deterministic web scraper that extracts a structured company profile from a given company website URL.

It is designed to be:
- Reliable and repeatable
- Free from hallucinated or inferred data
- Easy to review and extend

The scraper only extracts information that is explicitly present in the website HTML.

---

## What It Extracts
- Company name
- Description of what the company does
- Offerings (products/services)
- Proof signals (trust indicators)
- Contact page link
- Careers page link

If data is not found, the field is returned as null or an empty list.

---

## Project Structure

company_scraper/
├── fetcher.py
├── extractors.py
├── schemas.py
├── run.py
├── requirements.txt
└── sample_outputs/

---

## How It Avoids Hallucination
- Uses only visible HTML content
- No AI-generated text
- No guessing or inference
- Deterministic extraction rules

---

## How to Run

Install dependencies:
pip install -r requirements.txt

Run the scraper:
python run.py https://www.zoho.com

---

## Sample Outputs
Sample outputs for real websites are provided in the sample_outputs directory.

---

## Limitations
- JavaScript-heavy websites may return limited data
- Bot-protected sites may block requests

This is an intentional design choice to ensure reliability and repeatability.
