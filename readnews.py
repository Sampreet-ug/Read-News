import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
import pyttsx3

news_url="https://news.google.com/news/rss"
Client=urlopen(news_url)
xml_page=Client.read()
Client.close()

soup_page=soup(xml_page,"xml")
news_list=soup_page.findAll("item")
# Print news title, url and publish date
for news in news_list:
  print(news.title.text)
  print(news.link.text)
  print(news.pubDate.text)
  print("-"*60)

fname = "G:\\news.txt"
with open(fname,"w") as f:
  for news in news_list:
    f.write(news.title.text+"\n")

for news in news_list:
    engine = pyttsx3.init()
    engine.say(news.title.text)
    engine.runAndWait()
