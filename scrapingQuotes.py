import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import pandas as pd
import csv

options = Options()
options.add_experimental_option("detach", True)
options.add_argument("--log-level=3")

navegador = webdriver.Chrome(options=options)

navegador.get("https://quotes.toscrape.com/")
sleep(2)

page_content = navegador.page_source
site = BeautifulSoup(page_content, 'html.parser')

text_places = site.find_all('div', attrs={'class': 'quote'})

data_quotes = []

for text_place in text_places:
    text_place_quote = text_place.find('span', attrs={'itemprop': 'text'}).get_text(strip=True)
    text_place_author = text_place.find('small', attrs={'itemprop': 'author'}).get_text(strip=True)

    # Para também exibir no terminal as citações e autores
    print(f"Citação: {text_place_quote}")
    print(f"Autor: {text_place_author}")
    print("-" * 40)
    
    data_quotes.append([text_place_quote, text_place_author])

dados = pd.DataFrame(data_quotes, columns=['Citação', 'Autor'])
dados.to_csv('citacoes.csv', index=False, encoding="utf-8", quoting=csv.QUOTE_NONNUMERIC)
