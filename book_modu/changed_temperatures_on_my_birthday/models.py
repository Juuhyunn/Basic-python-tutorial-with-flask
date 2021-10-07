import csv
import matplotlib.pyplot as plt
from icecream import ic

'''
next()는 두 가지 포맷으로 사용된다.
1. consumer 구조로 사용할 땐 header를 제거한다.
2. function 구조로 사용할 땐 header를 반환한다.

row[날짜,지점,평균기온(℃),최저기온(℃),최고기온(℃)]
    최고기온은 [-1]이다.
    
data : [] = list()는 list타입의 data를 list()로 초기화하는 것이다.
단, 한 메소드 내에서만 사용하면 로컬에서 초기화하고,
예시)
data : [] = None
def save_highest_temperatures(self):
    data = list()
    
그러나, 여러 메소드에서 사용하면 필드에서 초기화한다.
예시)
data: [] = list()
'''


class ChangedTemperaturesOnMyBirthday(object):
    data: []
    highest_temperatures: [] = list()
    minimum_temperatures: [] = list()

    def preprocessing(self):
        self.read_data()
        self.save_data_to_list()
        self.visualize_data()
        self.extract_date_data()

    def read_data(self) -> object:
        data = csv.reader(open('../data/seoul.csv', encoding='utf-8'))
        next(data)
        self.data = data
        return data

    def show_highest_temperature(self):
        return [i[-1] for i in self.data]

    def save_highest_temperature(self):
        '''
        self.highest_temperatures = []
        self.minimum_temperatures = []
        [self.highest_temperatures.append(i[-1]) for i in self.read_data()]
        [self.minimum_temperatures.append(i[-2]) for i in self.read_data()]
        # ic(self.highest_temperatures)
        # ic(self.minimum_temperatures)
        '''
        [self.highest_temperatures.append(float(i[-1])) for i in self.data if i[-1] != '']
        # ic(self.highest_temperatures)
        ic(f'총 개수 : {len(self.highest_temperatures)}개')

    def visualize_data(self):
        plt.plot(self.highest_temperatures, 'lightpink')
        plt.plot(figsize=(20, 2))
        plt.show()

    def highest_temperatures_my_birthday(self):
        high = []
        low = []
        for i in self.data:
            if i[-1] != '' and i[-2] != '':
                if 1983 <= int(i[0].split('-')[0]):
                    if i[0].split('-')[1] == '03' and i[0].split('-')[2] == '05':
                        high.append(float(i[-1]))
                        low.append(float(i[-2]))
        plt.rc('font', family='Malgun Gothic')
        plt.rcParams['axes.unicode_minus'] = False
        plt.title('내 생일의 기온 변화 그래프')
        plt.plot(high, 'pink', label='high')
        plt.plot(low, 'skyblue', label='low')
        plt.legend()
        plt.show()
