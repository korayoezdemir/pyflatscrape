import requests
from models.flat import Flat

class BaseScraper:
    def __init__(self, city) -> None:
        self.city = city
        self.session = requests.Session()
        self.session.headers.update({'User-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'})
        self.flats: {Flat} = []