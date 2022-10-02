from datastructure.binarysearchtree.node import Node


class BinarySearchTree(object):

    def __init__(self, root):
        self.root = Node(root)

    def insert_node(self, new_value):
        BinarySearchTree.insert_helper(self.root, new_value)

    @staticmethod
    def insert_helper(current_node, new_value):
        if current_node.data < new_value:
            if current_node.right:
                BinarySearchTree.insert_helper(current_node.right, new_value)
            else:
                current_node.right = Node(new_value)
        else:
            if current_node.left:
                BinarySearchTree.insert_helper(current_node.left, new_value)
            else:
                current_node.left = Node(new_value)

    def search_node(self, value):
        return BinarySearchTree.search_helper(self.root, value)

    @staticmethod
    def search_helper(current_node, value):
        if current_node:
            if current_node.data == value:
                return True
            elif current_node.data < value:
                return BinarySearchTree.search_helper(current_node.right, value)
            else:
                return BinarySearchTree.search_helper(current_node.left, value)
        else:
            return False

    def is_bst(self):
        return BinarySearchTree.is_bst_helper(self.root)

    @staticmethod
    def is_bst_helper(current_node):
        if not current_node or not current_node.left or not current_node.right:
            return True
        current_node_data = current_node.data
        if current_node.left.data > current_node_data or current_node.right.data < current_node_data:
            return False
        elif current_node.left.data <= current_node_data:
            return BinarySearchTree.is_bst_helper(current_node.left)
        else:
            return BinarySearchTree.is_bst_helper(current_node.right)