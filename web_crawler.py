import requests
from bs4 import BeautifulSoup

def sites_crawler(max_pages):
    page = 1
    while page < max_pages:
        url = 'https://bigdata-madesimple.com/top-20-web-crawler-tools-scrape-websites/'