PHONY: install run-ebay run-immoscout
install:
	poetry install

run-ebay: install
	poetry run python ebay_scraper/main.py

run-immoscout: install
	poetry run python immoscout_scraper/main.py
