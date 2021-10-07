from bs4 import BeautifulSoup
from urllib.request import urlopen
from icecream import ic
'''
지원하는 Parser 종류
"html.parser" : 빠르지만 유연하지 않기 때문에 단순한 HTML문서에 사용합니다.
"lxml" : 매우 빠르고 유연합니다.
"xml" : XML 파일에만 사용합니다.
"html5lib" : 복잡한 구조의 HTML에 대해서 사용합니다.
'''


class BugsMusic(object):
    def __init__(self, url):
        self.url = url

    def scrap(self):
        soup = BeautifulSoup(urlopen(self.url), 'lxml')
        n_artists = 0;
        ls = soup.find_all(name='p', attrs={'class':'artist'})
        ls2 = soup.find_all(name = 'p', attrs= {'class':'title'})
        ic(f'List Size is {len(ls)}')
        for i, j in enumerate(ls):
            n_artists += 1
            ic(str(n_artists)+' Rank')
            ic('  Artist : ' + j.find('a').text)
            ic('  Title : ' + ls2[i].find('a').text)
            ic('*'*100)

    @staticmethod
    def main():
        BugsMusic(f'https://music.bugs.co.kr/chart/track/realtime/total?chartdate=20210720&charthour=16').scrap()


class BugsTest(object):
    def __init__(self, url):
        self.url = url

    def scrap(self):
        soup = BeautifulSoup(urlopen(self.url), 'lxml')
        n_artist = 0
        ls_artist = soup.find_all(name='p', attrs={'class': 'artist'})
        ls_title = soup.find_all(name='p', attrs={'class': 'title'})
        ic(f'Top {len(ls_artist)}!')
        for i, j in zip(ls_artist, ls_title):
            n_artist += 1
            ic(f'{n_artist} Rank')
            ic(f'Artist : {i.find("a").text}', end='\t\t')
            ic(f'Title : {j.find("a").text} ')
            ic('*'*100)

    @staticmethod
    def main():
        BugsTest('https://music.bugs.co.kr/chart/track/realtime/total?chartdate=20210721&charthour=10').scrap()
