from data_structures_and_algorithms.challenges.merge_sort.merge_sort import Mergesort


def test_simple_arr():
    arr = [8,4,23,42,16,15]
    Mergesort(arr)
    assert arr == [4, 8, 15, 16, 23, 42]

def test_list_reverse_order():
    arr = [42, 23, 16, 15, 8, 4]
    Mergesort(arr)
    assert arr == [4, 8, 15, 16, 23, 42]

def test_list_reverse_order2():
    arr = [20,18,12,8,5,-2]
    Mergesort(arr)
    assert arr == [-2, 5, 8, 12, 18, 20]

def test_list_zeros_and_negative():
    arr = [-23, -0.5, -4, 0, -1]
    Mergesort(arr)
    assert arr == [-23, -4, -1, -0.5, 0]

def test_few_uniques():
    arr = [5,12,7,5,5,7]
    Mergesort(arr)
    assert arr == [5, 5, 5, 7, 7, 12]

def test_nearly_sorted():
    arr = [2,3,5,7,13,11]
    Mergesort(arr)
    assert arr == [2, 3, 5, 7, 11, 13]

def test_sorted():
    arr = [2,3,5,7,11,13]
    Mergesort(arr)
    assert arr == [2,3,5,7,11,13]

def test_same_vals():
    arr = [1, 1, 1, 1, 1]
    Mergesort(arr)
    assert arr == [1, 1, 1, 1, 1]

def test_empty_list():
    arr = []
    Mergesort(arr)
    assert arr == []

def test_one_element():
    arr = [4]
    Mergesort(arr)
    assert arr == [4]

def test_two_elements():
    arr = [5, 4]
    Mergesort(arr)
    assert arr == [4, 5]

def test_strings():
    arr = ['cat','a', 'c', 'b']
    Mergesort(arr)
    assert arr == ['a', 'b', 'c', 'cat']
