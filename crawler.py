from bs4 import BeautifulSoup
from urllib.request import urlopen
from selenium import webdriver

import re
from nltk.tokenize import word_tokenize
from konlpy.tag import Okt
import pandas as pd
from nltk import FreqDist
from wordcloud import WordCloud
import matplotlib.pyplot as plt


class Model:
    def __init__(self):
        self._url = ''
        self._parser = ''
        self._path = ''
        self._api = ''

    @property
    def url(self) -> str: return self._url

    @url.setter
    def url(self, url): self._url = url

    @property
    def parser(self) -> str: return self._parser

    @parser.setter
    def parser(self, parser): self._parser = parser

    @property
    def path(self) -> str: return self._path

    @path.setter
    def path(self, path): self._path = path

    @property
    def api(self) -> str: return self._api

    @api.setter
    def api(self, api): self._api = api

class Service:
    def __init__(self):
        pass

    def bugs_music(self, payload):
        soup = BeautifulSoup(urlopen(payload.url), payload.parser)
        n_artist = 0
        n_title = 0
        for i in soup.find_all(name='p', attrs=({'class' : 'title'})):
            n_title += 1
            print(str(n_title)+'위')
            print('노래제목: {}'.format(i.text))

    def naver_movie(self, payload):
        driver = webdriver.Chrome(payload.path)
        driver.get(payload.url)
        soup = BeautifulSoup(urlopen(payload.url), payload.parser)
        # print(soup.prettify())
        arr = [div.a.string for div in soup.find_all('div', attrs={'class':'tit3'})]
        for i in arr:
            print(i)
        driver.close



class Controller:
    def __init__(self):
        self.service = Service()
        self.model = Model()

    def bugs_music(self, url):
        self.model.url = url
        self.model.parser = 'lxml'
        self.service.bugs_music(self.model)

    def naver_movie(self, url):
        self.model.url = url
        self.model.parser = 'html.parser'
        self.model.path = 'data/chromedriver.exe'
        self.service.naver_movie(self.model)

def print_menu():
   print('0.종료')
   print('1.벅스 크롤링')
   print('2.네이버 영화')
   return input('메뉴선택')
app = Controller()
while 1:
   menu = print_menu()
   if menu == '1':
       app.bugs_music('https://music.bugs.co.kr/chart/track/realtime/total?chartdate=20200625&charthour=12')
   if menu == '2':
       app.naver_movie('https://movie.naver.com/movie/sdb/rank/rmovie.nhn')
       break
   if menu == '0':
       break