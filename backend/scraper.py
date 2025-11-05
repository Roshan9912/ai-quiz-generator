import requests
from bs4 import BeautifulSoup

def scrape_wikipedia(url: str):
    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; WikiQuizBot/1.0; +https://github.com/yourusername/ai-quiz-generator)"
    }
    html = requests.get(url, headers=headers).content
    soup = BeautifulSoup(html, "html.parser")
    title_tag = soup.find("h1", {"id": "firstHeading"})
    if not title_tag:
        raise ValueError("Could not find article title in Wikipedia HTML (maybe a bot-blocked page or not a real Wikipedia article?)")
    title = title_tag.get_text()
    main_content = soup.select_one("div#mw-content-text")
    if not main_content:
        raise ValueError("Could not find content section in Wikipedia HTML.")
    for el in main_content(["sup", "table", "script", "style"]):
        el.decompose()
    paragraphs = [p.get_text() for p in main_content.find_all("p") if p.get_text(strip=True)]
    clean_text = "\n".join(paragraphs)
    sections = [h.get_text() for h in main_content.select("span.mw-headline")]
    return {
        "title": title,
        "clean_text": clean_text,
        "sections": sections,
        "raw_html": str(main_content)
    }

