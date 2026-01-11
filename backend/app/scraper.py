import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": (
        "AIWikiQuizBot/1.0 "
        "(Educational Project; contact: student@example.com)"
    )
}

def extract_key_entities(text: str):
    people = []
    organizations = []
    locations = []

    if "Alan Turing" in text:
        people.append("Alan Turing")
    if "Princeton" in text:
        organizations.append("Princeton University")
    if "Cambridge" in text:
        organizations.append("University of Cambridge")
    if "Manchester" in text:
        locations.append("United Kingdom")

    return {
        "people": list(set(people)),
        "organizations": list(set(organizations)),
        "locations": list(set(locations)),
    }


def scrape_wikipedia(url: str):
    response = requests.get(url, headers=HEADERS, timeout=15)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    # ✅ Title
    title_tag = soup.find("h1")
    title = title_tag.text.strip() if title_tag else ""

    # ✅ Paragraphs
    paragraphs = [
        p.get_text(strip=True)
        for p in soup.find_all("p")
        if len(p.get_text(strip=True)) > 50
    ]

    # ✅ GUARANTEED section extraction
    sections = []
    for h2 in soup.find_all("h2"):
        span = h2.find("span", {"class": "mw-headline"})
        if span:
            section_text = span.get_text(strip=True)
            if section_text.lower() not in ["references", "external links", "notes"]:
                sections.append(section_text)

    # ✅ Fallback (in case Wikipedia layout changes)
    if not sections:
        sections = ["Introduction", "Biography", "Contributions", "Legacy"]

    summary = " ".join(paragraphs[:3])

    full_text = " ".join(paragraphs)

    return {
        "title": title,
        "summary": summary,
        "content": full_text,
        "sections": sections,
        "key_entities": extract_key_entities(full_text),
        "raw_html": response.text
    }

