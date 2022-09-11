import random

from sorting import *

random_list = random.sample(range(-500, 500), 50)
sorted_list = [*range(1,50)]
duplicate_list = [random.randint(0,9) for _ in range(20)]
inverse_list = [*range(100)][::-1]
one_element_list = [1]

lists_to_check = [random_list, sorted_list, duplicate_list, inverse_list, one_element_list]

def check_sort(sort_function,lists_to_check):
    for _list in lists_to_check:
        assert sort_function(_list) == sorted(_list)


# insert sort
def test_insert_sort():
    check_sort(insert_sort, lists_to_check)

# quick sort
def test_quick_sort():
    check_sort(quick_sort, lists_to_check)

# selection sort
def test_selection_sort():
    check_sort(selection_sort, lists_to_check)

# bubble sort
def test_bubble_sort():
    check_sort(bubble_sort, lists_to_check)

# merge sort
def test_merge_sort():
    check_sort(merge_sort, lists_to_check)