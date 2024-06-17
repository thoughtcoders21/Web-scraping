import requests
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET


stock_gainers_url = "https://www.google.com/finance/markets/gainers"
stock_losers_url = "https://www.google.com/finance/markets/losers"


def store_stock_data_in_xml(url, title, xml_filename):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    main_div = soup.find('ul', class_='sbnBtf')

    if main_div:
        stock_items = main_div.find_all('li')

        root = ET.Element('Stocks')

        for item in stock_items:
            stock_name = item.find(class_='ZvmM7').text.strip()
            stock_price = item.find(class_='YMlKec').text.strip()
            gain_percentage = "↑"+item.find(class_='JwB6zf').text.strip()
            lose_percentage = "↓"+item.find(class_='JwB6zf').text.strip()

            stock_element = ET.SubElement(root, 'Stock')
            ET.SubElement(stock_element, 'Name').text = stock_name
            ET.SubElement(stock_element, 'Price').text = stock_price

            if title.lower() == 'gainers':
                stock_increment = item.find(class_='P2Luy Ez2Ioe').text.strip()
                ET.SubElement(stock_element, 'Increment').text = stock_increment
                ET.SubElement(stock_element, 'GainPercentage').text = gain_percentage
                ET.SubElement(stock_element, "\n")
            elif title.lower() == 'losers':
                stock_decrement = item.find(class_='P2Luy Ebnabc').text.strip()
                ET.SubElement(stock_element, 'Decrement').text = stock_decrement
                ET.SubElement(stock_element, 'LosePercentage').text = lose_percentage
                ET.SubElement(stock_element, "\n")


        tree = ET.ElementTree(root)
        tree.write(xml_filename, encoding='utf-8', xml_declaration=True)
        print(f"{title} data stored in {xml_filename}")
    else:
        print(f"Failed to retrieve {title.lower()} data from the website.")


store_stock_data_in_xml(stock_gainers_url, "Gainers", "gainers.xml")

store_stock_data_in_xml(stock_losers_url, "Losers", "losers.xml")
