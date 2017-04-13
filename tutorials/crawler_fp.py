# 使用函数式编程，point-free风格的网络爬虫

import requests
from bs4 import BeautifulSoup

fw = open('all_items.txt', 'a', encoding='utf-8')

# 复合函数
def compose(*fns):
    def composed(result):
        for fn in reversed(fns):
            result = fn(result)
        return result
    return composed

# 不完全函数
def partial(fn, *presetArgs):
    def partiallyApplied(*laterArgs):
        return fn(*presetArgs, *laterArgs)
    return partiallyApplied

# js-compatible map
def js_map(callback, iterable):
    new_list = [callback(it) for it in iterable]
    return new_list

# 返回商品列表页码
def generate_url(page):
    url = 'http://store.nba.com/Mens/pg/{0}/ps/84/so/no_sort'
    return url.format(page)

# 返回指定url地址符合条件的所有元素
def el_list(tag, filter_condition, url):
    res = requests.get(url)
    text = res.text
    soup = BeautifulSoup(text)
    return soup.find_all(tag, filter_condition)

# 返回指定url地址符合条件的指定元素
def el(tag, filter_condition, url):
    res = requests.get(url)
    text = res.text
    soup = BeautifulSoup(text)
    return soup.find(tag, filter_condition)

# 记录商品详情地址并返回
def record_item_href(item):
    href = item.get('href')
    fw.write(href + '\n')
    return href

# 记录商品描述
def record_item_detail(item):
    detail = item.string
    fw.write(detail + '\n')
 
# map(composed_items_of_all_pages(map((record_item_detail,item,record_item_href), (elements_of_items,generate_url))), range(1, 179))

# elements_of_items函数接收商品列表url返回指定页的所有商品元素
elements_of_items = partial(el_list, 'a', {'class': 'browseProductLink', 'itemprop': 'url'})

# element_of_item_detail函数返回指定商品详情页的元素
element_of_item_detail = partial(el, 'h1', {'class': 'section-headline'})

# composed_item函数接收一个商品详情的url，记录该url，到对应页面获取详情并记录
composed_item = compose(record_item_detail, element_of_item_detail, record_item_href)

# partial_item函数接收指定页面的所有item元素
partial_item = partial(js_map, composed_item)

# composed_items_of_page函数接收一个页码值，记录所有商品的url地址和详情
composed_items_of_page = compose(partial_item, elements_of_items, generate_url)

# partial_items_of_all_pages函数查询所有页面并记录所有信息
partial_items_of_all_pages = partial(js_map, composed_items_of_page, range(1, 179))

partial_items_of_all_pages()






