import requests
from bs4 import BeautifulSoup


stock_gainers = f"https://www.google.com/finance/markets/gainers"
stock_losers = f"https://www.google.com/finance/markets/losers"

response = requests.get(stock_gainers)
soup = BeautifulSoup(response.text, 'html.parser')
main_div = soup.find('ul', class_='sbnBtf')
if main_div:
    stock_items = main_div.find_all('li')

    for item in stock_items:
        stock_name = item.find(class_='ZvmM7').text.strip()
        stock_price = item.find(class_='YMlKec').text.strip()
        stock_increment = item.find(class_='P2Luy Ez2Ioe').text.strip()
        gain_percentage = "↑"+item.find(class_='JwB6zf').text.strip()
        print(f"Stock: {stock_name},Price: {stock_price},Increment: {stock_increment}, Gain: {gain_percentage}")
else:
    print("Failed to retrieve data from the website.")


response = requests.get(stock_losers)
soup = BeautifulSoup(response.text, 'html.parser')
main_div = soup.find('ul', class_='sbnBtf')
if main_div:
    stock_items = main_div.find_all('li')

    for item in stock_items:
        stock_name = item.find(class_='ZvmM7').text.strip()
        stock_price = item.find(class_='YMlKec').text.strip()
        stock_decrement = item.find(class_='P2Luy Ebnabc').text.strip()
        lose_percentage = "↓"+item.find(class_='JwB6zf').text.strip()
        print(f"Stock: {stock_name},Price: {stock_price},Decrement: {stock_decrement}, Lose: {lose_percentage}")
else:
    print("Failed to retrieve data from the website.")


