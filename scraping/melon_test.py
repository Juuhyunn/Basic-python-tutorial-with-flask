from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

class Melon(object):
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
            print(f'{n_artist} 위  :  {i.find("a").text} - {j.find("a").text}')
            print()

def main():
    Melon('https://www.melon.com/chart/index.htm?dayTime=2021072111').scrap()

if __name__ == '__main__':
    main()