import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

options = Options()
options.add_experimental_option("detach", True)
options.add_argument('window-size=400,800')
options.add_argument("--log-level=1")

navegador = webdriver.Chrome(options=options)

navegador.get("https://quotes.toscrape.com/")
sleep(2)

print(navegador.page_source)

site = BeautifulSoup(navegador.page_source,'html.parser')

print(site.prettify())