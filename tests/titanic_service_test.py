import unittest

from titanic.model.titanic_service import TitanicService


class TitanicServiceTest(unittest.TestCase):
    mock = TitanicService()

    def test_new_model(self):
        print(self.mock.new_model('train'))
        # print(self.mock.new_model('test'))


if __name__ == '__main__':
    unittest.main()