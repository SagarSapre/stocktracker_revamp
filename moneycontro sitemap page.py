import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import urlparse

url = "https://www.moneycontrol.com/sitemap.php"
headers = {"User-Agent": "Mozilla/5.0"}
html = requests.get(url, headers=headers).text

soup = BeautifulSoup(html, 'html.parser')
links = [a['href'] for a in soup.find_all('a', href=True) if a['href'].startswith("https://")]

# Optional: process links into hierarchy
data = []
for link in links:
    parsed = urlparse(link)
    parts = parsed.path.strip("/").split("/") if parsed.path.strip("/") else []
    parent = parts[-2] if len(parts) > 1 else ""
    child = parts[-1] if parts else ""
    depth = len(parts)
    data.append({
        "url": link,
        "parent": parent,
        "child": child,
        "depth": depth
    })

df = pd.DataFrame(data)
df.to_csv("moneycontrol_sitemap_from_html.csv", index=False)
print(f"Saved {len(df)} URLs from HTML")
