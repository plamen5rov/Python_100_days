from bs4 import BeautifulSoup
import requests

response = requests.get("https://appbrewery.github.io/instant_pot/")

web_page = response.text
soup = BeautifulSoup(web_page, 'html.parser')

price_whole = soup.find(name="span", class_="a-price-whole").getText()
price_fraction = soup.find(name="span", class_="a-price-fraction").getText()

price_combined = float(f"{price_whole}{price_fraction}")

print(price_combined)