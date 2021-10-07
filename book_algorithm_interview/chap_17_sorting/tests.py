import unittest
from book_algorithm_interview.chap_17_sorting.models import Sorting


class TestSorting(unittest.TestCase):
    def test_bubble_sort(self) -> []:
        instance = Sorting()
        instance.random_arr = [6, 3, 4, 5, 2, 1]
        self.assertEqual(instance.bubble_sort(), [1, 2, 3, 4, 5, 6])

    def test_merge_sort(self) -> []:
        res = Sorting.merge_sort([6, 3, 4, 5, 2, 1])
        self.assertEqual(res, [1, 2, 3, 4, 5, 6])

    def test_quick_sort(self) -> []:
        res = Sorting.quick_sort([6, 3, 4, 5, 2, 1])
        self.assertEqual(res, [1, 2, 3, 4, 5, 6])