from ebay_scraper.ebay import EbayScraper
from enums.enums import City
import time
import statistics
import pandas as pd

def run(all_cities=False, city=None):
    if all_cities:
        for city in City:
            process_city(city)
    elif city is not None:
        process_city(city)

def process_city(city):
    start_time = time.time()
    scraper = EbayScraper(city)
    scraper.scrape()
    print(f"Number of flats scraped in {city.value}: {len(scraper.flats)}")
    median_square_meter_prices = []
    
    for flat in scraper.flats:
        if isinstance(flat.price, float) and isinstance(flat.square_meters, float) and flat.square_meters != 0:
            median_square_meter_prices.append((flat.price / flat.square_meters))
        else:
            print("Price or square meters not available for this flat.")

    if median_square_meter_prices:
        median_price = statistics.median(median_square_meter_prices)
        super_cheap_flats = []
        for flat in scraper.flats:
            if isinstance(flat.price, float) and isinstance(flat.square_meters, float) and flat.square_meters != 0:
                if flat.price / flat.square_meters < median_price*0.80:
                    super_cheap_flats.append(flat)

        df = pd.DataFrame([flat.link for flat in super_cheap_flats])
        df.to_csv(f"{city.value}_cheap_flats.csv", index=False)

        print(f"Number of flats with price below median in {city.value}: {len(super_cheap_flats)}")
        print(f"Median square meter price in {city.value}: {median_price:.2f}")
    
    end_time = time.time()
    print(f"Time taken to scrape {city.value} : {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    # run(all_cities=True)  # Example to run for all cities or use run(city=City.BERLIN) for specific city
    run(city=City.KARLSRUHE)  # Example to run for all cities or use run(city=City.BERLIN) for specific city
