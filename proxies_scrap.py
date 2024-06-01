import requests
from bs4 import BeautifulSoup as bs
import xml.etree.ElementTree as ET


def scrap_proxies():
    url = "https://free-proxy-list.net/"
    response = requests.get(url)
    print(f"Requesting {url}, status code: {response.status_code}")
    if response.status_code == 200:
        soup = bs(response.content, 'html.parser')
        proxies = []
        table = soup.find("table", attrs={"class": "table-striped"})
        if not table:
            print("Table not found.")
            return proxies
        rows = table.find_all("tr")[1:]
        for row in rows:
            tds = row.find_all("td")
            if len(tds) < 2:
                continue
            ip = tds[0].text.strip()
            port = tds[1].text.strip()
            proxies.append({"ip": ip, "port": port})
        print(f"Found {len(proxies)} proxies. and saved in xml file")
        return proxies
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return []


def save_proxies_to_xml(proxies, filename):
    root = ET.Element("proxies")
    for proxy in proxies:
        proxy_element = ET.SubElement(root, "proxy")
        ip_element = ET.SubElement(proxy_element, "ip")
        ip_element.text = proxy["ip"]
        port_element = ET.SubElement(proxy_element, "port")
        port_element.text = proxy["port"]
        ET.SubElement(proxy_element, "\n")

    try:
        tree = ET.ElementTree(root)
        tree.write(filename, encoding='utf-8', xml_declaration=True)
        print(f"Proxies saved to {filename}")
    except Exception as e:
        print(f"Error saving proxies to {filename}: {e}")

proxies = scrap_proxies()

if proxies:
    save_proxies_to_xml(proxies, "proxies.xml")

