from scraping.models.dataset import Dataset
from scraping.models.service import Service


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

if __name__ == '__main__':
    view = View()
    view.modeling('melon.csv', 'bugs.csv')