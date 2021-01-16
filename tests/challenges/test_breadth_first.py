from data_structures_and_algorithms.data_structures.tree.tree import _Node, Queue, BinaryTree

def test_breadth_first_traversal1():
    bt = BinaryTree()
    bt.root = _Node(2) 
    bt.root.left = _Node(7) 
    bt.root.right = _Node(5) 
    bt.root.left.left = _Node(2) 
    bt.root.left.right = _Node(6)
    bt.root.left.right.left = _Node(5)
    bt.root.left.right.right = _Node(11)
    bt.root.right.right = _Node(9)
    bt.root.right.right.left = _Node(4)
    assert BinaryTree.breadth_first_traversal(bt.root) == [2,7,5,2,6,9,5,11,4]


def test_breadth_first_traversal2():
    bt = BinaryTree()
    bt.root = _Node(2) 
    assert BinaryTree.breadth_first_traversal(bt.root) == [2]