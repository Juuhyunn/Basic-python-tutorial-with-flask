import unittest

from basic.reverse_string.models import ReversString


class ReversStringTest(unittest.TestCase):
    mock = ReversString()
    def test_str_to_list(self):
        self.mock.str_to_list('a apple is good')

    def test_reverse_string(self):
        self.mock.reverse_string(self.mock.str_to_list('a apple is good'))

    def test_list_to_str(self):
        print(self.mock.list_to_str(self.mock.reverse_string(self.mock.str_to_list('a apple is good'))))

    def test_total(self):
        print(self.mock.total('hello'))

if __name__ == '__main__':
    unittest.main()