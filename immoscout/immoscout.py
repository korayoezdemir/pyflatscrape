import requests
from models import BaseScraper
from enums.enums import City

class ImmmoScoutScraper(BaseScraper):
    def __init__(self, city):
        self.url_templates = {
            City.BERLIN: "https://www.immobilienscout24.de/Suche/de/berlin/berlin/wohnung-mieten?pagenumber={}",
            City.MUNICH: "https://www.immobilienscout24.de/Suche/de/bayern/muenchen/wohnung-mieten?pagenumber={}",
            City.FRANKFURT: "https://www.immobilienscout24.de/Suche/de/hessen/frankfurt-am-main/wohnung-mieten?pagenumber={}",
            City.HAMBURG: "https://www.immobilienscout24.de/Suche/de/hamburg/hamburg/wohnung-mieten?pagenumber={}"
        }
        super().__init__(city)

    def scrape(self):
        response = requests.get(self.url_templates[self.city])
        print(response.content)