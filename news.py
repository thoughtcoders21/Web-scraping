import requests
from bs4 import BeautifulSoup

url = 'https://indianexpress.com/section/technology/'

response = requests.get(url)

if response.status_code == 200:

    soup = BeautifulSoup(response.content, 'html.parser')

    headlines = soup.find_all('h3', class_='')

    for headline in headlines:
        headline_text = headline.get_text(strip=True)

        print(f'Latest_Tech_News: {headline_text}')
else:
    print(f'Failed to retrieve the page. Status code: {response.status_code}')
