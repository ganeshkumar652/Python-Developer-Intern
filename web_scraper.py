import requests
from bs4 import BeautifulSoup

url = "https://news.ycombinator.com/"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")
headlines = soup.find_all("a", class_="storylink")

with open("headlines.txt", "w", encoding="utf-8") as file:
    for h in headlines:
        file.write(h.get_text(strip=True) + "\n")

print("Headlines saved to headlines.txt")
