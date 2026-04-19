import requests
from bs4 import BeautifulSoup
import pandas as pd

base_url = "http://quotes.toscrape.com/page/{}/"

data = []
page = 1

while True:
    url = base_url.format(page)
    print(f"Scraping page {page}...")

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print("No more pages or blocked.")
        break

    soup = BeautifulSoup(response.text, "html.parser")

    quotes = soup.find_all("span", class_="text")
    authors = soup.find_all("small", class_="author")

    if not quotes:
        print("No quotes found. Ending...")
        break

    for q, a in zip(quotes, authors):
        data.append({
            "quote": q.text,
            "author": a.text
        })

    # Check if "Next" button exists
    next_button = soup.find("li", class_="next")
    if not next_button:
        print("Reached last page.")
        break

    page += 1

# Save to CSV
df = pd.DataFrame(data)
df.to_csv("quotes.csv", index=False)

print(f"Scraping completed. Total quotes: {len(data)}")
