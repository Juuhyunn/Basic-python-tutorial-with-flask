from titanic.model.dataset import Dataset
from titanic.model.titanic_service import TitanicService


class TitanicView(object):
    dataset = Dataset()
    service = TitanicService()

    def modeling(self):
        this = self.service.preprocessing()
        return this

    def preprocessing(self) -> object:
        service = self.service
        this = self.dataset
        this.train = service.new_model('train')
        this.test = service.new_model('test')
        return this