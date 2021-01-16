from binarytree import tree, build
from data_structures_and_algorithms.data_structures.tree.tree import _Node, BinaryTree, BinarySearchTree, Queue
import pytest
@pytest.fixture
def my_bst():
    tree = BinarySearchTree()
    tree.add(15)
    tree.add(11)
    tree.add(13)
    tree.add(7)
    tree.add(8)
    tree.add(5)
    tree.add(19)
    tree.add(17)
    tree.add(23)
    return tree

def test_tree_instance():
    tree = BinaryTree()
    assert tree._root is None

def test_tree_one_member():
    tree = BinarySearchTree()
    tree.add('apples')
    assert tree._root.value == 'apples'

def test_add_three_members():
    tree = BinarySearchTree()
    tree.add(10)
    tree.add(5)
    tree.add(15)
    assert tree._root.value == 10
    assert tree._root.left.value == 5
    assert tree._root.right.value == 15

def test_add_more_members_for_balanced():
    tree = BinarySearchTree()
    tree.add(15)
    tree.add(11)
    tree.add(13)
    tree.add(7)
    tree.add(25)
    tree.add(60)
    tree.add(23)
    assert tree._root.value == 15
    assert tree._root.left.value == 11
    assert tree._root.right.value == 25
    assert tree._root.left.left.value == 7
    assert tree._root.left.right.value == 13
    assert tree._root.right.right.value == 60
    assert tree._root.right.left.value == 23

def test_add_more_members_for_imbalanced(my_bst):
    assert my_bst._root.value == 15
    assert my_bst._root.left.value == 11
    assert my_bst._root.left.right.value == 13
    assert my_bst._root.left.left.value == 7
    assert my_bst._root.left.left.left.value == 5
    assert my_bst._root.left.left.right.value == 8

def test_add_one_node():
    tree = BinarySearchTree()
    tree.add(20)
    assert tree._root.value == 20
    assert tree._root.left == None
    assert tree._root.right == None

def test_check_one_node_tree():
    tree = BinarySearchTree()
    tree.add(20)
    assert tree.contains(20) == True
    assert tree.contains(21) == False

def test_contains_true(my_bst):
    assert my_bst._root.value == 15
    assert my_bst.contains(7) == True
    assert my_bst.contains(9) == False

def test_pre_order(my_bst):
    assert my_bst.pre_order() == [15, 11, 7, 5, 8, 13, 19, 17, 23]

def test_pre_order_one():
    tree_one = BinarySearchTree()
    tree_one.add(20)
    assert tree_one.pre_order() == [20]

def test_in_order(my_bst):
    assert my_bst.in_order() == [5, 7, 8, 11, 13, 15, 17, 19, 23]
    
def test_post_order(my_bst):
    assert my_bst.post_order() == [5, 8, 7, 13, 11, 17, 23, 19, 15]

##################################
@pytest.fixture
def my_tree():
    values = [7, 3, 2, 6, 9, 10, 1, 5, 8]
    root = build(values)
    return root

@pytest.fixture
def my_tree2():
    values = [10, 134, 5, 23, 9, 10, 45, 32, 8]
    root = build(values)
    return root


def test_binarytree_module_build(my_tree):
    root = my_tree
    assert root.value == 7
    assert root.left.value == 3
    assert root.right.value == 2
    assert root.left.left.value == 6
    assert root.left.right.value == 9
    assert root.left.left.left.value == 5
    assert root.left.left.right.value == 8


def test_simply_tree_case(my_tree, my_tree2):
    tree1 = my_tree
    tree2 = my_tree2
    assert BinaryTree.tree_intersection(tree1, tree2) == {10,9,8,5}


def test_no_match(my_tree):
    tree1 = my_tree
    values = [100, 100, 100, 100]
    tree2 = build(values)
    assert BinaryTree.tree_intersection(tree1, tree2) == None

def test_everything_match(my_tree):
    tree1 = my_tree
    values = [7, 3, 2, 6, 9, 10, 1, 5, 8]
    tree2 = build(values)

    assert BinaryTree.tree_intersection(tree1, tree2) == {7, 3, 2, 6, 9, 10, 1, 5, 8}

def test_floats():
    tree1 = build([0.3, 5, -54, -3, 34])
    tree2 = build([-54, 95, 0.3, 123, 34])

    assert BinaryTree.tree_intersection(tree1, tree2) == {0.3, -54, 34}

def test_empty_tree():
    tree1 = build([])
    tree2 = build([3, 4])
    assert BinaryTree.tree_intersection(tree1, tree2) == None

def test_2nd_tree_is_empty():
    tree1 = build([3, 3, 4, 5])
    tree2 = build([])
    assert BinaryTree.tree_intersection(tree1, tree2) == None

def test_same_values():
    tree1 = build([10, 10, 10, 8])
    tree2 = build([10, 10, 10, 10, 10])
    assert BinaryTree.tree_intersection(tree1, tree2) == {10}