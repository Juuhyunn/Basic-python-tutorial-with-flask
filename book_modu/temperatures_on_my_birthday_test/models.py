import csv
import matplotlib.pyplot as plt


class TemperaturesOnMyBirthdayTest(object):
    data: [] = list()
    ls: [] = list()

    def read_data(self):
        data = csv.reader(open('../data/seoul.csv', encoding='utf-8'))
        next(data)
        self.data = data

    def save_data_to_list(self):
        return [self.ls.append(i) for i in self.data if i[-1] != '']

    def visualize_data(self):
        plt.plot()
        plt.show()

    def extracting_date(self):
        high = []
        low = []
        for i in self.ls:
            if 1983 <= int(i[0].split('-')[0]):
                if i[-1] != '' and i[-2] != '':
                    if i[0].split('-')[-1] == '03' and i[0].split('-')[-2] == '05':
                        high.append(float(i[-1]))
                        low.append(float(i[-2]))
        plt.rc('font', family='Malgun Gothic')
        plt.rcParams['axes.unicode_minus'] = False
        plt.title('내 생일의 기후 변화')
        plt.plot(high, 'r', label='High')
        plt.plot(low, 'g', label='Low')
        plt.legend()
        plt.show()

