from titanic.model.dataset import Dataset
import pandas as pd

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


    def embarked_nominal(this: object) -> object:
        return this


    def fare_ordinal(this: object) -> object:
        return this


    def title_nominal(this: object) -> object:
        return this


    def gender_nominal(this: object) -> object:
        return this


    def age_nominal(this: object) -> object:
        return this


    def create_k_fold() -> {}:
        return None


    def accuracy_by_classfier(this: object) -> str:
        return ""