import requests
from bs4 import BeautifulSoup

with open('feeds.txt') as f:
    feeds = []
    for line in f:
        feeds.append(line)

for feed in feeds:
    url = feed.strip()

    resp = requests.get(url)

    soup = BeautifulSoup(resp.content, features="xml")

    news_items_list = []

    items = soup.findAll('item')

    for item in items:
        news_items = {}
        news_items['title'] = item.title.text
        news_items['description'] = item.description.text
        news_items['link'] = item.link.text
        news_items['pubDate'] =item.pubDate.text
        news_items_list.append(news_items)

    num = 0
    for  article in news_items_list:
        print(article['title'])
        print(article['link'])
        num += 1
        if num == 10:
            break

