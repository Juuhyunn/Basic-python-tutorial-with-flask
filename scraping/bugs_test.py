from bs4 import BeautifulSoup
from urllib.request import urlopen

class Bugs(object):
    def __init__(self, url):
        self.url = url

    def scrap(self):
        soup = BeautifulSoup(urlopen(self.url), 'lxml')
        n_artist = 0
        ls_artist = soup.find_all(name='p', attrs={'class': 'artist'})
        ls_title = soup.find_all(name='p', attrs={'class': 'title'})
        print(f'Top {len(ls_artist)}!')
        for i, j in zip(ls_artist, ls_title):
            n_artist += 1
            print(f'{n_artist} Rank')
            print(f'Artist : {i.find("a").text}', end='\t\t')
            print(f'Title : {j.find("a").text} ')
            print('*'*100)


def main():
    Bugs('https://music.bugs.co.kr/chart/track/realtime/total?chartdate=20210721&charthour=10').scrap()

if __name__ == '__main__':
    main()