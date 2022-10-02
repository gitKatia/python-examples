from datastructure.binarysearchtree.binarysearchtree import BinarySearchTree

if __name__ == '__main__':
    binarySearchTree = BinarySearchTree(10)
    binarySearchTree.insert_node(4)
    binarySearchTree.insert_node(2)
    binarySearchTree.insert_node(26)
    binarySearchTree.insert_node(8)
    binarySearchTree.insert_node(14)

    print(binarySearchTree.search_node(19))
    print(binarySearchTree.search_node(14))

    print(binarySearchTree.is_bst())

    binarySearchTree = BinarySearchTree(11)
    print(binarySearchTree.is_bst())