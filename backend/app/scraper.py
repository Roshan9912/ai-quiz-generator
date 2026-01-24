import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0 Safari/537.36"
    )
}

def scrape_wikipedia(url: str):
    response = requests.get(url, headers=HEADERS, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    # Title
    title = soup.find("h1").get_text(strip=True)

    # Paragraphs
    paragraphs = [
        p.get_text(strip=True)
        for p in soup.find_all("p")
        if p.get_text(strip=True)
    ]

    # ✅ Summary = first 2 paragraphs
    summary = " ".join(paragraphs[:2])

    # Clean text for LLM
    clean_text = " ".join(paragraphs[:10])[:15000]

    # Sections
    sections = [
    h.text.strip()
    for h in soup.select("h2 span.mw-headline")
    if h.text.strip()
]


    return {
        "title": title,
        "summary": summary,
        "clean_text": clean_text,
        "sections": sections,
        "raw_html": response.text
    }
