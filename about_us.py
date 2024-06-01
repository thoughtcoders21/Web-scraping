import requests
from bs4 import BeautifulSoup
import re


def scrape_contact_info(urls):
    all_contacts = []
    for url in urls:
        response = requests.get(url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')

            about_us_link = soup.find('a', string=re.compile(r'about us', re.IGNORECASE))

            if about_us_link:
                about_us_url = about_us_link.get('href')

                about_us_response = requests.get(about_us_url)

                if about_us_response.status_code == 200:

                    about_us_soup = BeautifulSoup(about_us_response.content, 'html.parser')

                    contact_info = about_us_soup.find_all(string=re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b|\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b'))

                    contacts = [contact.strip() for contact in contact_info]
                    all_contacts.extend(contacts)
                else:
                    print("Failed to retrieve the 'About Us' page {}. Status code: {}".format(about_us_url, about_us_response.status_code))
            else:
                print("No 'About Us' link found on the webpage {}.".format(url))
        else:
            print("Failed to retrieve the webpage {}. Status code: {}".format(url, response.status_code))

    return all_contacts


if __name__ == "__main__":
    urls = ["https://thoughtcoders.com"]
    contact_info = scrape_contact_info(urls)

    if contact_info:
        print("Contact information found:")
        for contact in contact_info:
            print(contact)
    else:
        print("No contact information found.")
