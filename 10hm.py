import requests
from bs4 import BeautifulSoup

URL = "http://books.toscrape.com/"


def scrape_first_page_prices():
    try:
        response = requests.get(URL)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        books = soup.select("article.product_pod")

        prices = [book.select_one("p.price_color").text for book in books]

        return prices
    except Exception as e:
        print(f"Виникла помилка: {e}")
        return []


prices = scrape_first_page_prices()

print(f"Знайдено книг на сторінці: {len(prices)}\n")
for price in prices:
    print(price)