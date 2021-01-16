from data_structures_and_algorithms.challenges.array_binary_search.array_binary_search import (
    BinarySearch
)


def test_if_number_is_exist():
    actual = BinarySearch([4,8,15,16,23,42], 15)
    expected = 2
    assert actual == expected

def test_if_number_not_exist():
    actual = BinarySearch([11,22,33,44,55,66,77], 90)
    expected = -1
    assert actual == expected

def test_if_list_is_empty():
    actual = BinarySearch([],9)
    expected = "the list is empty"
    assert actual == expected


# def test_wrong_input():
#     actual = BinarySearch([],9)
#     expected = "You have entered wrong  input"
#     assert actual == expected

