import requests
from bs4 import BeautifulSoup
import operator


def start(url):
    word_list = []
    source_code = requests.get(url, "html.parser").text
    soup = BeautifulSoup(source_code, features="html.parser")
    for post_text in soup.findAll('a', {'class': 'index_singleListingTitles'}):
        content = post_text.string
        words = content.lower().split()
        for each_word in words:
            print(each_word)
            word_list.append(each_word)


start('https://en.wikipedia.org/wiki/Web_scrapingr')
