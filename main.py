import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import pandas as pd

options = Options()
options.add_experimental_option("detach", True)
# options.add_argument('window-size=400,800')
options.add_argument("--log-level=3")

navegador = webdriver.Chrome(options=options)

navegador.get("https://quotes.toscrape.com/")
sleep(2)

page_content = navegador.page_source
site = BeautifulSoup(page_content, 'html.parser')

data_quotes = []

text_places = site.find_all('div', attrs={'class': 'quote'})

# print(text_place.prettify())

for text_place in text_places:
    text_place_quote = text_place.find('span', attrs={'itemprop': 'text'})
    text_place_author = text_place.find('small', attrs={'itemprop': 'author'})

    elements = [
        (text_place_quote, "Citação"), 
        (text_place_author, "Autor")
    ]

    for element, label in elements:
        if element:
            text = element.get_text(strip=True)
            print(f"{label}: {text}")
        else:
            print("Elemento não encontrado")
    
    data_quotes.append([text_place_quote, text_place_author])

dados = pd.DataFrame(data_quotes, columns=['Citação', 'Autor'])
dados.to_csv('citacoes.csv', index=False)
