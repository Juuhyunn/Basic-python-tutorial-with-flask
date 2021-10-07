import csv
import matplotlib.pyplot as plt
import numpy
from icecream import ic


class Population(object):
    data: [] = list()

    def read_data(self):
        data = csv.reader(open('../data/202106_202106_연령별인구현황_월간.csv', encoding='utf-8'))
        next(data)
        self.data = list(data)

    def pop_per_dong(self, dong: str) -> []:
        for i in self.data:
            if dong in i[0]:
                ic('a')
                arr = numpy.array(i[3:], dtype=int) / int(i[2].replace(',', ''))
        # for i in self.data:
        #     arr2 = numpy.array(i[3:], dtype=int) / int(i[2].replace(',', ''))
        #     print('aaa')
        #     print(arr1 - arr2)
        return arr

    def show_plot(self, arr: []):
        plt.rc('font', family='Malgun Gothic')
        plt.title('인구구조')
        plt.style.use('ggplot')
        plt.plot(arr)
        plt.show()


