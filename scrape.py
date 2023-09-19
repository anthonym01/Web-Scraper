# Web scraper example

from urllib import request


url_to_scrape = 'https://github.com/anthonym01/Web-Scraper'


def scrape(url):
    # Get the HTML of the page
    print('Scraping ' + url)

scrape(url_to_scrape)