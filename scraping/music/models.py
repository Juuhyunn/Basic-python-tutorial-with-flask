from bs4 import BeautifulSoup
import requests
import pandas as pd
from icecream import ic
from common.menu.models import Menu

from dataclasses import dataclass


@dataclass
class Dataset(object):
    context: str
    fname: str
    bugs: object
    melon: object

    @property
    def context(self) -> str: return self._context
    @context.setter
    def context(self, context): self._context = context
    @property
    def fname(self) -> str: return self._fname
    @fname.setter
    def fname(self, fname): self._fname= fname
    @property
    def bugs(self) -> object: return self._bugs
    @bugs.setter
    def bugs(self, bugs): self._bugs = bugs
    @property
    def melon(self) -> object: return self._melon
    @melon.setter
    def melon(self, melon): self._melon = melon


class Service(object):
    dataset = Dataset()

    def new_modeling(self, payload):
        this = self.dataset
        this.context = '../data/'
        this.fname = payload
        return pd.read_csv(this.context + this.fname)


class Music(object):
    domain = ''
    query_string = ''
    html = ''
    headers = {'User-Agent': 'Mozilla/5.0'}
    tag_name = ''
    fname = ''
    class_name = []
    artists = []
    titles = []
    dict = {}
    df = None

    def set_html(self):
        self.html = requests.get(f'{self.domain}{self.query_string}', headers=self.headers).text
        ic(f'Crawling HTML : {self.html}')

    def get_ranking(self):
        _ = 0
        soup = BeautifulSoup(self.html, 'lxml')
        all1 = soup.find_all(name=self.tag_name, attrs={'class': self.class_name[0]})
        all2 = soup.find_all(name=self.tag_name, attrs={'class': self.class_name[1]})

        for i, j in zip(all1, all2):
            _ += 1
            ic(f'{self.fname} : {_}위. {i.find("a").text}  - {j.find("a").text}')
            self.artists.append(i.find("a").text)
            self.titles.append(j.find("a").text)

    def insert_dict(self):
        '''
        #방법 1
        for i in range(0, len(self.tag_name)):
            self.dict[self.titles[i]] = self.artists[i]
        #방법 2
        for i, j in zip(self.titles, self.artists):
            self.dict[i]= j
        #방법 3
        for i,j in enumerate(self.titles):
            self.dict[j] = self.artists[i]
        '''

        for i, j in zip(self.titles, self.artists):
            self.dict[i] = j
        ic(self.dict)

    def dic_to_dataframe(self):
        self.df = pd.DataFrame.from_dict(self.dict, orient='index')
        ic(self.df)

    def df_to_csv(self):
        path = f'../data/{self.fname}_211007.csv'
        self.df.to_csv(path, sep=',', na_rep='NaN', encoding="utf-8-sig")

    @staticmethod
    def main():
        mr = Music()
        while 1:
            menu = Menu.print_menu(['Exit', 'Input time', 'Output', 'Print dict', 'dict to Dataframe', 'Df to csv'])
            if menu == 0:
                break
            elif menu == 1:
                m1 = Menu.print_menu(['melon', 'bugs'])
                if m1 == 0:
                    mr.fname = 'melon'
                    mr.domain = 'https://www.melon.com/chart/index.htm?dayTime='
                    mr.query_string = '2021072015'
                else:
                    mr.fname = 'bugs'
                    mr.domain = 'https://music.bugs.co.kr/chart/track/realtime/total?'
                    mr.query_string = 'chartdate=20210721&charthour=10'
                mr.set_html()
            elif menu == 2:
                if m1 == 0:
                    mr.tag_name = 'div'
                    mr.class_name.append('ellipsis rank02')
                    mr.class_name.append('ellipsis rank01')
                else:
                    mr.tag_name = 'p'
                    mr.class_name.append('artist')
                    mr.class_name.append('title')
                mr.get_ranking()
            elif menu == 3:
                mr.insert_dict()
            elif menu == 4:
                mr.dic_to_dataframe()
            elif menu == 5:
                mr.df_to_csv()


class View(object):
    dataset = Dataset()
    service = Service()

    def modeling(self, melon, bugs):
        this = self.preprocessing(melon, bugs)
        print('*'*100)
        print(f'The Type of the This {type(this)}')
        print('*'*100)
        print(f'The Head of the Melon \n{this.melon.head(5)}')
        print('*'*100)
        print(f'The Head of the Bugs \n{this.bugs.head(5)}')
        print('*'*100)

    def preprocessing(self, melon, bugs):
        service = self.service
        this = self.dataset
        this.melon = service.new_modeling(melon)
        this.bugs = service.new_modeling(bugs)
        return this
