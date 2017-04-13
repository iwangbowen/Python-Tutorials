import requests
from bs4 import BeautifulSoup

fw = open('items.txt', 'a', encoding='utf-8')
gear_url = 'http://store.nba.com/Mens/pg/{0}/ps/72/so/no_sort'
def spider(max_pages):
    page = 1
    while page < max_pages:
        try:
            print('page: ', page)
            res = requests.get(gear_url.format(page))
            plain_text = res.text
            soup = BeautifulSoup(plain_text)
            for link in soup.findAll('a', {'class': 'browseProductLink', 'itemprop': 'url'}):
                href = link.get('href')
                fw.write(href + '\n')
                get_single_item_data(href)
            page += 1
        except:
            print('Exception happened when fatch all items of a page')
        
def get_single_item_data(item_url):
    try:
        res = requests.get(item_url)
        plain_text = res.text
        soup = BeautifulSoup(plain_text)
        for item_name in soup.find_all('h1', {'class': 'section-headline'}):
            name = item_name.string
            fw.write(name + '\n')
    except:
        print('Exception happened when fetching a single item')

spider(207)


