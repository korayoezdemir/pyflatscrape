from bs4 import BeautifulSoup
import time
from enums.enums import City
from models.basescraper import BaseScraper
from models.flat import EbayFlat

class EbayScraper(BaseScraper):
    def __init__(self, city):
        self.url_template = {
            City.BERLIN: "https://www.kleinanzeigen.de/s-wohnung-mieten/berlin/anzeige:angebote/seite:{}/c203l3331",
            City.MUNICH: "https://www.kleinanzeigen.de/s-wohnung-mieten/muenchen/anzeige:angebote/seite:{}/c203l6411", # strange
            City.FRANKFURT: "https://www.kleinanzeigen.de/s-wohnung-mieten/frankfurt-am-main/anzeige:angebote/seite:{}/c203l3331",
            City.HAMBURG: "https://www.kleinanzeigen.de/s-wohnung-mieten/hamburg/anzeige:angebote/seite:{}/c203l9409",
            City.KARLSRUHE: "https://www.kleinanzeigen.de/s-wohnung-mieten/karlsruhe/anzeige:angebote/seite:{}/c203l9186"
        }
        super().__init__(city)
        

    def scrape(self, page_range=5):
        time.sleep(1)
        for page_number in range(1, page_range+1):
           
            url = self.url_template[self.city].format(page_number)
            print(url)
            response = self.session.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')

            list_items = soup.find_all('li', class_='ad-listitem')

            for item in list_items:
                if item.find('article', class_='aditem'):
                    data = self.parse_item(item)
                    self.flats.append(data)

            # Pause to avoid overloading the website
            time.sleep(1)

    def parse_item(self, item):
        try:
            # Ensure that the title exists before proceeding
            title_element = item.find('h2', class_='text-module-begin')
            title_element_clean = title_element.get_text(strip=True).replace("[]", '').lower() if title_element else ''
            title = title_element_clean if title_element else 'Title not available'

            # Ensure that the link exists
            link_element = item.find('a', class_='ellipsis')
            link = link_element['href'] if link_element else 'Link not available'

            # Ensure that the description exists
            desc_element = item.find('p', class_='aditem-main--middle--description')
            description = desc_element.get_text(strip=True) if desc_element else 'Description not available'

            # Extract price with improved error handling
            price_element = item.find('p', class_='aditem-main--middle--price-shipping--price')
            if price_element:
                price_text = price_element.get_text(strip=True).replace('€', '').replace('.', '').replace(',', '.').replace('VB', '').strip()
                price = float(price_text) if price_text.isdigit() else 'Price not available'
            else:
                price = 'Price not available'

            sm_element = item.find('span', class_='simpletag')
            if sm_element:
                sm_text = sm_element.get_text(strip=True).replace('m²', '').replace(',', '.').strip()
                sm = float(sm_text) if sm_text.replace('.', '', 1).isdigit() else 'Square meters not available'
            else:
                sm = 'Square meters not available'

            # Process additional data like location and handle all possible errors
            location_element = item.find('div', class_='aditem-main--top--left')
            location = location_element.get_text(strip=True) if location_element else 'Location not available'
            return EbayFlat(title, price, location, sm, description, link)

        except Exception as e:
            print(f"Error parsing item: {e}")
            return EbayFlat("Error", 0, "Error", 0, "Error")