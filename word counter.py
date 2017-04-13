import requests
from bs4 import BeautifulSoup
import operator

url = 'http://store.nba.com/Mens/pg/1/ps/84/so/no_sort'
def start(url):
    word_list = []
    text = requests.get(url).text
    soup = BeautifulSoup(text)
    for link in soup.findAll('a', {'class': 'browseProductLink', 'itemprop': 'url'}):
        content = link.string
        words = content.lower().split()
        for each_word in words:
            word_list.append(each_word)
    print(word_list)

# is it possible to implement this feature using functionnal programming
start(url)