from unittest import TestCase

from based_indexing import list


class TestList(TestCase):

    def test_get_list_length(self):
        my_list = list()
        self.assertEqual(len(my_list), 0)

    def test_get_list_length_with_elements(self):
        my_list = list(1, 2, 3)
        self.assertEqual(len(my_list), 3)

    def test_get_all_list(self):
        my_list = list(1, 2, 3)
        self.assertEqual(my_list["all"], [1, 2, 3])

    def test_list_indexing(self):
        my_list = list()
        my_list.append(1)
        my_list.append(2)
        my_list.append(3)

        self.assertEqual(my_list["first"], 1)
        self.assertEqual(my_list["last"], 3)
        self.assertEqual(my_list["middle"], 2)
        self.assertEqual(my_list["all"], [1, 2, 3])

    def test_list_slicing(self):
        my_list = list(1, 2, 3, 4, 5, 6)
        self.assertEqual(my_list["second":"fourth"], [2, 3])
        self.assertEqual(my_list[:"middle":"second"], [1, 3])
        self.assertEqual(my_list[::"second"], [1, 3, 5])

    def test_iter_list(self):
        iter = []
        my_list = list(1, 2, 3)
        for item in my_list:
            iter.append(item)
        self.assertEqual(iter, my_list["all"])

    def test_iter_range_list(self):
        iter = []
        my_list = list(1, 2, 3, 4)
        for item in my_list["first":"middle"]:
            iter.append(item)
        self.assertEqual(iter, [1, 2])
