import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep

options = Options()
options.add_experimental_option("detach", True)
options.add_argument("--log-level=3")

navegador = webdriver.Chrome(options=options)

navegador.get("https://books.toscrape.com/")
sleep(2)

page_content = navegador.page_source
site = BeautifulSoup(page_content, 'html.parser')

# print(site.prettify())

book_places = site.find_all('article', attrs={'class': 'product_pod'})

for book_place in book_places:
    book_title = book_place.h3.a['title']
    book_price = book_place.find('p', attrs={'class': 'price_color'}).get_text(strip=True)
    book_disponibility = book_place.find('p', attrs={'class': 'instock availability'}).get_text(strip=True)

    print(f"Titulo do livro: {book_title}")
    print(f"Preço: {book_price}")
    print(f"Disponibilidade: {book_disponibility}")

    navegador.find_element(By.XPATH, f"//a[@title='{book_title}']").click()

    sleep(2)
    page_content = navegador.page_source
    site = BeautifulSoup(page_content, 'html.parser')

    book_qtd = site.find('p', attrs={'class': 'instock availability'}).get_text(strip=True)
    print(f"Quantidade em estoque: {book_qtd}")
    navegador.back()