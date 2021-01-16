import pytest
from data_structures_and_algorithms.challenges.linked_list.linked_list import Node, LinkedList, create_list_insert, create_list_append, zip_Lists


def test_1slist_shorter():
    l_list1 = create_list_append(['a', 'b', 'c', 'd'])
    l_list2 = create_list_append(['e','f','g','h','i'])
    ref_to_head = zip_Lists(l_list1, l_list2)
    assert ref_to_head.value == "a"
    assert l_list1.__str__() == '{ a } -> { e } -> { b } -> { f } -> { c } -> { g } -> { d } -> { h } -> { i } -> { none }'

def test_1slist_longer():
    l_list1 = create_list_insert(['d', 'c', 'b', 'a', 'z'])
    l_list2 = create_list_insert(['h','g','f','e'])
    ref_to_head = zip_Lists(l_list1, l_list2)
    assert ref_to_head.value == "z"
    assert l_list1.__str__() == '{ z } -> { e } -> { a } -> { f } -> { b } -> { g } -> { c } -> { h } -> { d } -> { none }'


def test_lists_equal():
    l_list1 = create_list_append(['L', 'U', 'A', 'A'])
    l_list2 = create_list_append(['T','C','S','C'])
    ref_to_head = zip_Lists(l_list1, l_list2)
    assert ref_to_head.value == "L"
    assert l_list1.__str__() == '{ L } -> { T } -> { U } -> { C } -> { A } -> { S } -> { A } -> { C } -> { none }'


def test_lists_empty():
    l_list1 = LinkedList()
    l_list2 = LinkedList()
    with pytest.raises(Exception):
        zip_Lists(l_list1, l_list2)

def test_list_1st_empty():
    l_list1 = LinkedList()
    l_list2 = create_list_insert(['d', 'c', 'b', 'a'])
    ref_to_head = zip_Lists(l_list1, l_list2)
    assert ref_to_head.value == "a"
    assert l_list1.__str__() == '{ a } -> { b } -> { c } -> { d } -> { none }'

def test_list_2nd_empty():
    l_list2 = LinkedList()
    l_list1 = create_list_insert(['d', 'c', 'b', 'a'])
    ref_to_head = zip_Lists(l_list1, l_list2)
    assert ref_to_head.value == "a"
    assert l_list1.__str__() == '{ a } -> { b } -> { c } -> { d } -> { none }'

def test_list_1st_1element():
    l_list1 = create_list_insert([1])
    l_list2 = create_list_insert(['d', 'c', 'b', 'a'])
    ref_to_head = zip_Lists(l_list1, l_list2)
    assert ref_to_head.value == 1
    assert l_list1.__str__() == '{ 1 } -> { a } -> { b } -> { c } -> { d } -> { none }'

def test_list_2ndlist_1element():
    l_list1 = create_list_insert(['d', 'c', 'b', 'a'])
    l_list2 = create_list_insert([1])
    ref_to_head = zip_Lists(l_list1, l_list2)
    assert ref_to_head.value == 'a'
    assert l_list1.__str__() == '{ a } -> { 1 } -> { b } -> { c } -> { d } -> { none }'

def test_includes():
    create_list_insert([1,2,3,4,5])    
    expected = True
    actual = create_list_insert([1,2,3,4,5]).includes(4)
    assert expected == actual

def test_append_and_multiple_append():
    create_list_append([0,1,2,3])
    expected = "{ 0 } -> { 1 } -> { 2 } -> { 3 } -> { none }"
    actual = create_list_append([0,1,2,3]).__str__()
    assert expected == actual


def test_insertAfter_at_middle():
    test=create_list_append([0,1,2,3])
    test.insertAfter(1,'im middle')
    expected = "{ 0 } -> { 1 } -> { im middle } -> { 2 } -> { 3 } -> { none }"
    actual = test.__str__()
    assert expected == actual


def test_insertAfter_at_last():
    test=create_list_append([0,1,2,3])
    test.insertAfter(3,'at last')
    expected = "{ 0 } -> { 1 } -> { 2 } -> { 3 } -> { at last } -> { none }"
    actual = test.__str__()
    assert expected == actual


def test_insertBefore_at_first():
    test=create_list_append([0,1,2,3])
    test.insertBefore(0,'at_first')
    expected = "{ at_first } -> { 0 } -> { 1 } -> { 2 } -> { 3 } -> { none }"
    actual = test.__str__()
    assert expected == actual


def test_insertBefore_at_middle():
    test=create_list_append([0,1,2,3])
    test.insertBefore(2,'at_middle')
    expected = "{ 0 } -> { 1 } -> { at_middle } -> { 2 } -> { 3 } -> { none }"
    actual = test.__str__()
    assert expected == actual

def test_kthFromEnd_1():
    test=create_list_append([0,1,2,3])
    expected = 3
    actual =test.kthFromEnd(0)
    assert expected == actual

def test_kthFromEnd_2():
    test=create_list_append([0,1,2,3])
    expected = 1
    actual =test.kthFromEnd(2)
    assert expected == actual

def test_kthFromEnd_3():
    test=create_list_append([0,1,2,3])
    expected = 'value not found'
    actual =test.kthFromEnd(7)
    assert expected == actual

def test_kthFromEnd_4():
    test=create_list_append([0,1,2,3,4,5,6,7,8])
    expected = 0
    actual =test.kthFromEnd(8)
    assert expected == actual

def test_kthFromEnd_5():
    test=create_list_append([0,1,2,3,4,5,6,7,8])
    expected = 'value not found'
    actual =test.kthFromEnd(-8.64)
    assert expected == actual