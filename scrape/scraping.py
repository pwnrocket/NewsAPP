import requests
from bs4 import BeautifulSoup
from xml.etree import ElementTree
from .models import *
import time


HEADERS =  {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36"}


def get_story(url):

    soup = BeautifulSoup(requests.get(url,headers=HEADERS,timeout=160).text,'html.parser')
    story_div = soup.find('div',class_="story-detail")
    all_p = story_div.find_all('p')
    story = ""
    for p in all_p:
        story = story + p.text
    
    return story

def Scrape():
    r =  requests.get("https://www.thenews.com.pk/rss/1/1",timeout=160)

    tree = ElementTree.fromstring(r.content)

    all_items = tree.findall("channel/item")

    for item in all_items:
        title = item.find('title').text
        url = item.find('link').text
        story = get_story(url)
        published = item.find('pubDate').text
        author = "The News International"
        authorid,_ = Author.objects.get_or_create(name=author)
        articleid,__ = Article.objects.get_or_create(title=title,body=story,author=authorid,url=url,pub_date=published)
        time.sleep(20)