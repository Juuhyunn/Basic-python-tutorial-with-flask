from django.db import models
# 모델은 정형화 되어 있는 샘플 데이터(진짜 데이터) 를 가지고 있는 데이터프레임
# 데이터를 가지고 있지 않는 데이터 프레임은 데이터 스트럭쳐?
# Create your models here.
from icecream import ic
import pandas as pd

from common.crime_common.models import ValueObject, Printer, Reader

class CrimeCctvMode(object):
    vo = ValueObject()
    printer = Printer()
    reader = Reader()

    def __init__(self):
        '''
        features of Raw data
        살인 발생,살인 검거,강도 발생,강도 검거,강간 발생,강간 검거,절도 발생,절도 검거,폭력 발생,폭력 검거
        '''
        self.crime_columns = ["살인 발생", "강도 발생", "강간 발생", "절도 발생", "폭력 발생"] # Nominal
        self.arrest_columns = ["살인 검거", "강도 검거", "강간 검거", "절도 검거", "폭력 검거"] # Nominal
        self.arrest_rate_columns = ["살인 검거율", "강도 검거율", "강간 검거율", "절도 검거율", "폭력 검거율"] # Ratio

    def merge_crime_cctv(self):

        crime_model = self.reader.csv('../crime/data/new_data/police_positions')
        # self.printer.dframe(crime_model)
        # print(crime_model.loc[0]['구별'])
        crime_model = crime_model.drop(['관서명'], axis=1)
        # self.printer.dframe(crime_model)
        crime = crime_model[self.crime_columns]
        arrest = crime_model[self.arrest_columns]
        gu = crime_model["구별"]
        # print(crime.loc[1])
        # print("*"*100)
        # test = 0
        # test = sum([i for i in crime.loc[0]])
        # print(test)
        # print("*"*100)
        crime_ls = []
        arrest_ls = []
        # for i in range(len(crime.index)):
        #     crime.loc[i, '총합'] = [sum([int(j) for j in crime.loc[i]])]
        #     crime_ls.append(sum([int(j) for j in crime.loc[i]]))
        [crime_ls.append(sum([int(j) for j in crime.loc[i]])) for i in range(len(crime.index))]
        [arrest_ls.append(sum([int(j) for j in arrest.loc[i]])) for i in range(len(arrest.index))]
        print(type(crime_ls))
        crime['발생 총합'] = crime_ls
        arrest['검거 총합'] = arrest_ls
        result = pd.concat([gu, crime['발생 총합'], arrest['검거 총합']], axis=1)
        grouped = result.groupby('구별')
        crime_filter = grouped['발생 총합', '검거 총합'].sum()
        crime_filter.to_csv('../crime/data/new_data/test.csv')
        # test = pd.DataFrame(columns=crime_model.columns)
        # self.printer.dframe(test)
        # for i in range(len(crime_model.index)-1):
        #     if i == 0:
        #         pass
        #     elif crime_model.loc[i]['구별'] == crime_model.loc[i-1]['구별']:
        #         for s in range(len(crime_model.columns)-3):
        #             test.loc[i,s] = [crime_model.loc[i][s] + crime_model.loc[i-1][s]]
        # merge.to_csv('admin/crime/data/new_data/test.csv')



        # list =
        # crime = crime_model['발생':f'{sum(i) for i in }']
        # self.printer.dframe(crime)
        # print("*"*100)
        # self.printer.dframe(arrest)
        # print("*"*100)
        # # print(crime[''])