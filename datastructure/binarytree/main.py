from datastructure.binarytree.binarytree import BinaryTree
from datastructure.binarytree.node import Node

if __name__ == '__main__':
    tree = BinaryTree("A")
    tree.root.left = Node("B")
    tree.root.right = Node("C")
    tree.root.left.left = Node("D")
    tree.root.left.right = Node("E")
    tree.root.right.left = Node("F")
    tree.root.right.right = Node("G")

    tree.print_tree("pre-order")
    tree.print_tree("in-order")
    tree.print_tree("post-order")
    tree.print_tree("level-order")
    tree.print_tree("x-order")
