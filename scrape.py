# Web scraper example

from urllib.request import urlopen

homeRepo = 'https://github.com/anthonym01/Web-Scraper'
urltoScrape = homeRepo

def inputlink():
    urltoScrape = input("Enter a Url to scrape: ")
    if urltoScrape == "" or urltoScrape == " ":
        urltoScrape=homeRepo
    scrape(urltoScrape)

def scrape(url):
    # Get the HTML of the page
    print('Scraping ' + url)

inputlink()# Starting point