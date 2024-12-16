import requests
from bs4 import BeautifulSoup
from difflib import SequenceMatcher

def similarity_ratio(title1, title2):
    return SequenceMatcher(None, title1, title2).ratio() * 100

query = "amaliyot hisoboti agrobank"
url = f"https://www.google.com/search?q={query}"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")
search_results = soup.find_all("div", class_="tF2Cxc")

for result in search_results:
    title = result.find("h3").text
    link = result.find("a")["href"]
    print("Title:", title)
    print("similarity_ratio:", similarity_ratio(title, query))
    print("Link:", link)
    print("-" * 50)
