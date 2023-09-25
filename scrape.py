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
    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    print('Scraping complete, got the HTML: ')
    print(html)
    pageTitle = findTitleinhtml(html)
    

def findTitleinhtml(html):
    # Find the title
    title_index = html.find("<title>") + len("<title>")
    end_title_index = html.find("</title>")
    title = html[title_index:end_title_index]
    print('Page title: '+title)
    return title

def findLinks(html):
    # Find all links
    a_index = html.find("<a href=")
    while a_index != -1:
        # Find the link URL
        link_start = html.find('"', a_index)
        link_end = html.find('"', link_start + 1)
        link = html[link_start + 1:link_end]
        print(link)
        # Find the next link
        a_index = html.find("<a href=", link_end)

inputlink()# Starting point
