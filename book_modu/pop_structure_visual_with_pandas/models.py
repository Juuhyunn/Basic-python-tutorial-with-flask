import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
# rc('font', family=font_manager.FontProperties(fname='C:/Windows/Fonts/malgun.ttf').get_name())
from icecream import ic


class Population(object):
    data: [] = list()
    result_name: str = ''
    home: None = list()
    away: None = list()

    def read_data(self):
        df = pd.read_csv('../data/202106_202106_연령별인구현황_월간.csv', encoding='utf-8', index_col=0, thousands=',')
        # print(df)
        df.to_csv('./data/202106_202106_연령별인구현황_월간_without_comma.csv', sep=',', na_rep='NaN')
        data = csv.reader(open('../data/202106_202106_연령별인구현황_월간_without_comma.csv', encoding='utf-8'))
        next(data)
        self.data = list(data)

    def pop_per_dong(self, dong: str) -> []:
        mn = 1
        self.read_data()
        for i in self.data:
            if dong in i[0]:
                arr1 = np.array(i[3:], dtype=int) / int(i[2])
        self.read_data()
        for i in self.data:
            arr2 = np.array(i[3:], dtype=int) / int(i[2])
            s = np.sum((arr1-arr2)**2)
            if s < mn and dong not in i[0]:
                mn = s
                dong2 = i[0]
                # result = arr2
        plt.rc('font', family='Malgun Gothic')
        plt.plot(arr1, label=dong)
        plt.plot(arr2, label=dong2)
        plt.legend()
        plt.show()

    def show_plot(self, arr: []) :
        # plt.rc('font', family='Malgun Gothic')
        plt.title('인구 차이?')
        plt.style.use('ggplot')
        plt.plot(arr)
        plt.show()

    def find_home(self, name):
        home = []
        [home.append(int(j)) for i in self.data if name in i[0] for j in i[3:]]
        self.home = home

    def array_to_list(self, arr: object) -> []:
        return arr.to_list()

    def list_to_array(self, ls: []) -> object:
        return np.array(ls)

    def show_plot_home(self, arr: object, name: str):
        plt.title(f'{name} 지역의 인구 구조')
        plt.plot(arr)
        plt.show()

    def find_similar_area(self, name: str):
        mn = 1
        result = 0
        home = None
        for i in self.data:
            if name in i[0]:
                home = np.array(i[3:], dtype=int) / int(i[2])
        ic(type(home))
        self.home = home
        for i in self.data:
            away = np.array(i[3:], dtype=int) / int(i[2])
            s = np.sum((home-away)**2)
            if s < mn and name not in i[0]:
                mn = s
                self.result_name = i[0]
                result = away
        self.away = result

    def show_plot_similar_two_cities(self, name: str, home: [], away: []):
        plt.style.use('ggplot')
        plt.figure(figsize=(10, 5), dpi=300)
        plt.title(f'{name} 지역과 가장 비슷한 인구 구조를 가진 지역')
        plt.plot(home, label=name)
        plt.plot(away, label=self.result_name)
        plt.legend()
        plt.show()
