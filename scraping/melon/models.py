from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.request import Request
from icecream import ic


class MelonMusic(object):
    def __init__(self, url):
        self.url = url

    def scrap(self):
        soup = BeautifulSoup(urlopen(Request(self.url, headers = {'User-Agent':'Mozilla/5.0'}) ), 'lxml')
        n_artist = 0
        ls_artist = soup.find_all(name='div', attrs={'class': 'ellipsis rank02'})
        ls_title = soup.find_all(name='div', attrs={'class': 'ellipsis rank01'})
        for i, j in enumerate(ls_artist):
            n_artist += 1
            ic(f'[ {n_artist} Rank ]  artist : {j.find("a").text}\t\ttitle : {ls_title[i].find("a").text}')
            ic('*'*100)

    @staticmethod
    def main():
        MelonMusic('https://www.melon.com/chart/index.htm?dayTime=2021072109').scrap()


class MelonTest(object):
    def __init__(self, url):
        self.url = url
        self.headers = {'User-Agent': 'Mozilla/5.0'}

    def scrap(self):
        soup = BeautifulSoup(urlopen(Request(self.url, headers=self.headers)), 'lxml')
        n_artist = 0
        ls_artist = soup.find_all(name='div', attrs={'class': 'ellipsis rank02'})
        ls_title = soup.find_all(name='div', attrs={'class': 'ellipsis rank01'})
        for i, j in zip(ls_artist, ls_title):
            n_artist += 1
            ic(f'{n_artist} 위  :  {i.find("a").text} - {j.find("a").text}')
            ic('*'*100)

    @staticmethod
    def main():
        MelonTest('https://www.melon.com/chart/index.htm?dayTime=2021072111').scrap()