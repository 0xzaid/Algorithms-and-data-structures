import unittest
import sys
import os
import random

current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
from Bubble_sort import bubble_sort


class bubble_sort_tests(unittest.TestCase):
    def bubble_sort(self, lst):
        copy = lst[:]
        bubble_sort(copy)
        return copy
        
    def test_empty_list(self):
        lst = []
        sorted_lst = self.bubble_sort(lst)
        self.assertEqual(lst, sorted_lst)
        
    def test_single_item(self):
        lst = [1]
        sorted_lst = self.bubble_sort(lst)
        self.assertEqual(lst, sorted_lst)
    
    def test_two_items_sorted(self):
        lst = [1, 2]
        sorted_lst = self.bubble_sort(lst)
        self.assertEqual(lst, sorted_lst)
        
    def test_two_items_unsorted(self):
        lst = [10, 9]
        sorted_lst = self.bubble_sort(lst)
        self.assertEqual(sorted_lst, [9, 10])
        
    def test_zero_in_list(self):
        lst = [1, 0]
        sorted_lst = self.bubble_sort(lst)
        self.assertEqual(sorted_lst, [0, 1])
        
    def test_odd_number_of_items(self):
        lst = [16, 6, 1]
        sorted_lst = self.bubble_sort(lst)
        self.assertEqual(sorted_lst, [1, 6, 16])
        
    def test_even_number_of_items(self):
        lst = [25, 7, 15, 3]
        sorted_lst = self.bubble_sort(lst)
        self.assertEqual(sorted_lst, [3, 7, 15, 25])

    def test_duplicate_integers_in_list(self):
        lst = [1, 3, 3, 1, 0, 0, 16, 16]
        sorted_lst = self.bubble_sort(lst)
        self.assertEqual(sorted_lst, [0, 0, 1, 1, 3, 3, 16, 16])

    def test_larger_integers(self):
        lst = [581753, 1000000, 142, 58625, 58928592852, 10, 456]
        sorted_lst = self.bubble_sort(lst)
        self.assertEqual(sorted_lst,
                [10, 142, 456, 58625, 581753, 1000000, 58928592852])
        
    def test_random(self):
        lst = [5,1,6,10,65,25,-15,0,3]
        sorted_lst = self.bubble_sort(lst)
        self.assertEqual(sorted_lst, [-15, 0, 1, 3, 5, 6, 10, 25, 65])
        
    def test_small_random(self):
        small_list = []
        for i in range(0,10):
            n = random.randint(1,1000)
            small_list.append(n)
        sorted_lst = self.bubble_sort(small_list)
        self.assertEqual(sorted_lst, sorted(small_list))
    
    def test_medium_random(self):
        medium_list = []
        for i in range(0,100):
            n = random.randint(1,1000)
            medium_list.append(n)
        sorted_lst = self.bubble_sort(medium_list)
        self.assertEqual(sorted_lst, sorted(medium_list))

    def test_large_random(self):
        large_list = []
        for i in range(0,1000):
            n = random.randint(1,1000)
            large_list.append(n)
        sorted_lst = self.bubble_sort(large_list)
        self.assertEqual(sorted_lst, sorted(large_list))

if __name__ == '__main__':
    unittest.main()