# Python Web Scraping Project

This project is designed to scrape data from various websites, focusing on collecting information about cheap flats in different cities in Germany. It uses Python as the primary language and leverages libraries such as `requests`, `beautifulsoup4`, and `pandas` for web scraping and data manipulation.

## Project Structure

- `berlin_cheap_flats.csv`, `frankfurt_cheap_flats.csv`, `hamburg_cheap_flats.csv`, `karlsruhe_cheap_flats.csv`, `muenchen_cheap_flats.csv`: CSV files containing scraped data of cheap flats in respective cities.
- `ebay/`: Contains scripts for scraping data from eBay.
- `enums/`: Defines various enumerations used across the project.
- `immoscout/`: Contains scripts for scraping data from ImmobilienScout24.
- `models/`: Defines data models, including the base scraper and flat model.

## Dependencies

- Python 3.11
- requests
- beautifulsoup4
- pandas
- openpyxl

These dependencies are managed using Poetry. The `pyproject.toml` file contains all the necessary configuration.