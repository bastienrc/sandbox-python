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
# print(title)

# line = ''
# for i in range(len(title)):
#     line += '-'
# print(line)

quotes = []
for quote in soup.find_all("div", class_="quote"):
    text = quote.find("span", class_="text").text
    author = quote.find("small", class_="author").text
    # .text version abrégé de .get_text()
    # tags = quote.find_all("div", class_="tags").text
    # print(f'{text} by {author}')
    quotes.append([text, author])


# On enregistre dans un fichier csv
with open(f'{os.path.dirname(__file__)}/{title}.csv', mode='w', newline='') as file:
    fieldnames = ['text', 'author']
    writer = csv.writer(file)
    writer.writerow(fieldnames)
    for quote in quotes:
        writer.writerow(quote)

