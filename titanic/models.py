import pandas as pd

from titanic.model.dataset import Dataset
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import seaborn as sns

rc('font', family=font_manager.FontProperties(fname='C:/Windows/Fonts/malgun.ttf').get_name())

'''
Titanic's features
PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked
'''


class TitanicService(object):
    dataset = Dataset()

    def new_model(self, payload) -> object:
        # this = self.dataset
        # this.context = '/data/'
        # this.fname = 'payload'
        # print(this.context + this.fname)
        return pd.read_csv(f'../data/{payload}.csv')

    @staticmethod
    def create_train(this: object) -> object:
        return this.train.drop('Survived', axis=1)

    @staticmethod
    def create_label(this: object) -> {}:
        return this.train['Survived']

    @staticmethod
    def drop_feature(this: object, *feature) -> object:
        for i in feature:
                this.train = this.train.drop([i], axis=1)
                this.test = this.test.drop([i], axis=1)
        return None

    @staticmethod
    def embarked_nominal(this: object) -> object:
        return this

    @staticmethod
    def fare_ordinal(this: object) -> object:
        return this

    @staticmethod
    def title_nominal(this: object) -> object:
        return this

    @staticmethod
    def gender_nominal(this: object) -> object:
        return this

    @staticmethod
    def age_nominal(this: object) -> object:
        return this

    @staticmethod
    def create_k_fold(self) -> {}:
        return None

    @staticmethod
    def accuracy_by_classfier(this: object) -> str:
        return ""


class Plot(object):
    data = Dataset()
    service = TitanicService()

    def __init__(self):
        self.df = self.service.new_model('train.csv')  # object is datafram

    def show_plot_survived_dead(self):
        this = self.df
        f, ax = plt.subplots(1, 2, figsize=(18, 8))
        series = this['Survived'].value_counts()
        print(type(series))
        print(series)
        series.plot.pie(explode=[0, 0.1], autopct='%1.1f%%', ax=ax[0], shadow=True)
        ax[0].set_title('0. 사망자 vs 1. 생존자')
        ax[0].set_ylabel('')
        ax[1].set_title('0. 사망자 vs 1. 생존자')
        sns.countplot('Survived', data=this, ax=ax[1])
        plt.show()

    def show_plot_pclass(self):
        this = self.df
        this['생존 결과'] = this['Survived'].replace(0, '사망자').replace(1, '생존자')
        this['좌석 등급'] = this['Pclass'].replace(1, '일등석').replace(2, '이등석').replace(3, '삼등석')
        sns.countplot(data=this, x='좌석 등급', hue='생존 결과')
        plt.show()

    def show_plot_embarked(self):
        # C: 쉘버그 S: 사우스햄튼 Q:퀸즈 타운
        this = self.df
        this['생존 결과'] = this['Survived'].replace(0, '사망자').replace(1, '생존자')
        this['Embarked'] = this['Embarked'].replace('C', '쉘버그').replace('S', '사우스햄튼').replace('Q', '퀸즈타운')
        sns.countplot(data=this, x='Embarked', hue='생존 결과')
        plt.show()

    def show_plot_sex(self):
        this = self.df
        f, ax = plt.subplots(1, 2, figsize=(18, 8))
        male_series = this['Survived'][this['Sex'] == 'male'].value_counts()
        female_series = this['Survived'][this['Sex'] == 'female'].value_counts()
        male_series.plot.pie(explode=[0, 0.1], autopct='%1.1f%%', ax=ax[0], shadow=True)
        female_series.plot.pie(explode=[0, 0.1], autopct='%1.1f%%', ax=ax[1], shadow=True)
        ax[0].set_title('남성의 생존 비율 0. 사망자 vs 1. 생존자')
        ax[1].set_title('여성의 생존 비율 0. 사망자 vs 1. 생존자')
        plt.show()
