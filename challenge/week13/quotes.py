import os,re
import requests
import urllib.request as ur
from bs4 import BeautifulSoup as bs
from collections import Counter
from operator import itemgetter

url='https://quotes.toscrape.com/tag/life/'
html=ur.urlopen(url)
soup=bs(html.read(),'html.parser')
quotes=soup.find_all('div',{"class":"quote"})
for quote in quotes:
    quote = quote.find_all('span',{"class":"text"})
    for i in quote:
        print(i.text)
#텍스트를 모아두기
all_text = ' '.join([quote.find('span', {'class': 'text'}).text for quote in quotes])

word_frequencies = Counter(all_text.lower().split())

# 빈도가 높은 상위 5개 단어 출력
top_words = dict(word_frequencies).items()
top_words = sorted(top_words, key=itemgetter(1), reverse=True)[:5]
print("상위 5개의 단어와 빈도수:")
for word, frequency in top_words:
    print("{}: {}".format(word,frequency))