import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

quotes = soup.find_all("span", class_="text")
authors = soup.find_all("small", class_="author")

for q, a in zip(quotes, authors):
    print(q.text, "-", a.text)
import pandas as pd

data = []

for q, a in zip(quotes, authors):
    data.append({
        "quote": q.text,
        "author": a.text
    })

df = pd.DataFrame(data)
print(df.head())
df.to_csv("quotes.csv", index=False)

print("Scraping completed and data saved to quotes.csv")