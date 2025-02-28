import requests
from bs4 import BeautifulSoup
import psycopg2

# Database connection
conn = psycopg2.connect(
    dbname="cdp_chatbot",
    user="postgres",  # Apna username
    password="admin",  # Apna password
    host="localhost",
    port="5432"
)
cur = conn.cursor()

# URLs
urls = {
    "Segment": "https://segment.com/docs/",
    "mParticle": "https://docs.mparticle.com/",
    "Lytics": "https://docs.lytics.com/",
    "Zeotap": "https://docs.zeotap.com/home/en-us/"
}

def scrape_page(url, platform):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # Yeh simple hai, real mein tumhe specific sections dhoondhne padenge
    content = soup.get_text()
    cur.execute(
        "INSERT INTO cdp_docs (platform, section, content) VALUES (%s, %s, %s)",
        (platform, "home", content)
    )
    conn.commit()

# Har CDP ka data scrape karo
for platform, url in urls.items():
    print(f"Scraping {platform}...")
    scrape_page(url, platform)

cur.close()
conn.close()