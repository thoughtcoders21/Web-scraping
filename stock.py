import requests
from bs4 import BeautifulSoup
import time

stock = "INFY"
stock_url = f"https://www.google.com/finance/quote/{stock}:NSE"

for i in range(9999):
    response = requests.get(stock_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    data = "YMlKec fxKbKc"
    stock_price = float(soup.find(class_=data).text.strip()[1:].replace(",",""))
    print(stock_price)
    time.sleep(5)