from datastructure.binarytree.node import Node
from datastructure.queue.queue import Queue


class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, traversal_type):
        if "pre-order" == traversal_type:
            print("Pre order:", "->".join(BinaryTree.pre_order_list(self.root, [])))
        elif "in-order" == traversal_type:
            print("In order:", "->".join(BinaryTree.in_order_list(self.root, [])))
        elif "post-order" == traversal_type:
            print("Post order:", "->".join(BinaryTree.post_order_list(self.root, [])))
        elif "level-order" == traversal_type:
            print("Level order:", "->". join(BinaryTree.level_order_list(self.root)))
        else:
            print("Unsupported traversal type", traversal_type)

    @staticmethod
    def pre_order_list(node, traversal_list):
        # Depth-first traversal
        if node:
            traversal_list.append(str(node.value))
            BinaryTree.pre_order_list(node.left, traversal_list)
            BinaryTree.pre_order_list(node.right, traversal_list)
        return traversal_list

    @staticmethod
    def in_order_list(node, traversal_list):
        # Depth-first traversal
        if node:
            BinaryTree.in_order_list(node.left, traversal_list)
            traversal_list.append(str(node.value))
            BinaryTree.in_order_list(node.right, traversal_list)
        return traversal_list

    @staticmethod
    def post_order_list(node, traversal_list):
        # Depth-first traversal
        if node:
            BinaryTree.post_order_list(node.left, traversal_list)
            BinaryTree.post_order_list(node.right, traversal_list)
            traversal_list.append(str(node.value))
        return traversal_list

    @staticmethod
    def level_order_list(node):
        # Breadth-first traversal
        if not node:
            return

        queue = Queue()
        queue.enqueue(node)

        traversal_list = []
        while len(queue) > 0:
            node = queue.dequeue()
            traversal_list.append(str(node.value))

            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)

        return traversal_list

    @staticmethod
    def height(node):
        # height is measured from leaves
        if not node:
            return -1
        left_height = BinaryTree.height(node.left)
        right_height = BinaryTree.height(node.right)
        return 1 + max(left_height, right_height)

    @staticmethod
    def size(node):
        if not node:
            return 0
        left_size = BinaryTree.size(node.left)
        right_size = BinaryTree.size(node.right)
        return 1 + left_size + right_size

