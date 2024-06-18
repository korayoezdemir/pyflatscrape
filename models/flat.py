class Flat:
    def __init__(self, title, price, location, square_meters, description, link):
        self.title = title
        self.price = price
        self.location = location
        self.square_meters = square_meters
        self.description = description
        

    def __repr__(self):
        return f"Flat(title={self.title}, price={self.price}, location={self.location}, square_meters={self.square_meters}, description={self.description}, link={self.link})"
    
class EbayFlat(Flat):
    def __init__(self, title, price, location, square_meters, description, link):
        super().__init__(title, price, location, square_meters, description, link)
        self.link = "https://www.kleinanzeigen.de" + link

class ImmoScoutFlat(Flat):
    def __init__(self, title, price, location, square_meters, description, link):
        super().__init__(title, price, location, square_meters, description, link)
        self.link = "https://www.immobilienscout24.de" + link