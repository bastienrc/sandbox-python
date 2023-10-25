import requests
from bs4 import BeautifulSoup
import csv
import os

# Quotes.toscrape.com est un atelier de web scraping pour débutants, contenant une liste paginée de citations.
url = "https://quotes.toscrape.com"
reponse = requests.get(url)
page = reponse.content

soup = BeautifulSoup(page, "html.parser")

title = soup.title.string
print(title)

line = ''
for i in range(len(title)):
    line += '-'
print(line)

quotes = []
for quote in soup.find_all("div", class_="quote"):
    text = quote.find_all("span", class_="text")[0].text
    author = quote.find_all("small", class_="author")[0].text
    # tags = quote.find_all("div", class_="tags").text

    print(f'{text} by {author}')
    # quotes.append(text)
