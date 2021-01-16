from binarytree import tree, build
class _Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.next = None

class Queue:

    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        """
        method to check if Queue is empty
        """
        if self.front == None:
            return True
        return False

    def enqueue(self, node):
        """
        Method that takes any value as an argument and adds a new node with that value to the back of the queue
        """
        new_node = node
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        """
        Method that removes the node from the front of the queue, and returns the node's value.
        """
        if not self.is_empty():
            temp = self.front
            self.front = self.front.next
            temp.next = None
            return temp
        else:
            return None

    def peek(self):
        """
        Method that returns the value of the node located in the front of the queue, without removing it from the queue
        """
        if not self.is_empty():
            return self.front.value
        return None

class BinaryTree:
    def __init__(self):
        self._root = None
    def pre_order(self, node=None, arr = None):
        """
        Method to return an array of trre values in "pre-order" order
        """
        if arr is None:
            arr = []
        node = node or self._root
        arr.append(node.value)
        if node.left:
            self.pre_order(node.left, arr)
        if node.right:
            self.pre_order(node.right, arr)
        return arr

    def in_order(self, node=None, arr = None):
        """
        Method to return an array of tree values "in-order" 
        """
        if arr is None:
            arr = []
        node = node or self._root
        if node.left:
            self.in_order(node.left, arr)
        arr.append(node.value)
        if node.right:
            self.in_order(node.right, arr)
        return arr

    def post_order(self, node=None, arr = []):
        """
        Method to return an array of tree values "post-order"
        """
        node = node or self._root
        if node.left:
            self.post_order(node.left, arr)
        if node.right:
            self.post_order(node.right, arr)
        arr.append(node.value)
        return arr

    def find_maximum_value(self):
        """ An instance method that returns the maximum value stored in the tree"""

        q = Queue()

        if not self._root:
            return None

        max_ = self._root.value
        q.enqueue(self._root)

        while not q.is_empty():
            node_front = q.dequeue()

            max_ = max(max_, node_front.value)


            if node_front.left:
                q.enqueue(node_front.left)
            if node_front.right:
                q.enqueue(node_front.right)

        return max_


    def breadth_first_traversal(root): 
        '''
        function which takes a Binary Tree root as its unique input and returns a list of the values in the tree in the order they were encountered:
            inp ---> the root of the inputed tree
            out >>> a list of the values in the tree in the order they were encountered
        '''
        breadth, result = [], []
        
        if root:
            result.append(root)
        while len(result) > 0:
            current = result.pop(0)
            breadth.append(current.value)
            if current.left:
                result.append(current.left)
            if current.right:
                result.append(current.right)
                
        return breadth
    

    def tree_intersection(tree1, tree2):
        tree1_set = BinaryTree.n_pre_order(tree1)
        set_result = BinaryTree.n_pre_order2(tree2, tree1_set)
        if set_result == set():
            return None
        else:
            return set_result
            


    def n_pre_order(tree, node=None, tree_set=None):
        if tree == None:
            return None
        if tree_set is None:
            tree_set = set()

        node = node or tree

        tree_set.add(node.value)
        if node.left:
            BinaryTree.n_pre_order(tree, node.left, tree_set)
        if node.right:
            BinaryTree.n_pre_order(tree, node.right, tree_set)
        return tree_set

    def n_pre_order2(tree, tree_set, node=None, set_result=None):
        if tree_set == None or tree == None:
            return None
        if set_result is None:
            set_result = set()

        node = node or tree

        if node.value in tree_set:
            set_result.add(node.value)

        if node.left:
            BinaryTree.n_pre_order2(tree, tree_set, node.left, set_result)
        if node.right:
            BinaryTree.n_pre_order2(tree, tree_set, node.right, set_result)
        return set_result


class BinarySearchTree(BinaryTree):
    def add(self, value):
        """
        Method that accepts a value, and adds a new node with that value in the correct location in the binary search tree
        """
        node = _Node(value)
        if not self._root:
            self._root = node
            return
        current = self._root
        while True:
            if node.value < current.value:
                if current.left:
                    current = current.left
                else:
                    current.left = node
                    return
            else:
                if current.right:
                    current = current.right
                else:
                    current.right = node
                    return
                    
    def contains(self,value):
        """
        Method that accepts a value, and returns a boolean indicating whether or not the value is in the tree at least once
        """
        if self._root == None:
            raise "Tree is empty"
        current = self._root
        while current:
            if current.value == value:
                return True
            if current.value > value:
                current = current.left
            else:
                current = current.right
        return False