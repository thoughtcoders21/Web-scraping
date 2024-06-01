import requests
from bs4 import BeautifulSoup
import re
import xml.etree.ElementTree as ET


def scrape_contact_info(urls):
    all_emails = []
    for url in urls:
        response = requests.get(url)

        if response.status_code == 200:

            soup = BeautifulSoup(response.content, 'html.parser')

            email_elements = soup.find_all(string=re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'))

            email_addresses = [email.strip() for email in email_elements]
            all_emails.extend(email_addresses)
        else:
            print("Failed to retrieve the webpage {}. Status code: {}".format(url, response.status_code))

    return all_emails


def create_xml(contact_info):
    root = ET.Element("ContactInfo")
    for email in contact_info:
        ET.SubElement(root, "Email").text = email

    tree = ET.ElementTree(root)
    tree.write("contact_info.xml")


if __name__ == "__main__":
    urls = ["https://thoughtcoders.com"]
    contact_info = scrape_contact_info(urls)

    if contact_info:
        print("Contact information found:")
        for email in contact_info:
            print(email)

        create_xml(contact_info)
        print("Contact information stored in 'contact_info.xml'")
    else:
        print("No contact information found on the webpages.")
