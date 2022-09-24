from datastructure.doublylinkedlist.node import Node


class DoublyLinkedList:

    def __init__(self):
        self.head = None

    def add_node_after(self, key, data):
        node = self.find_node_by_key(key)
        if not node:
            return
        new_node = Node(data)
        new_node.next = node.next
        new_node.previous = node.previous
        node.next = new_node

    def add_node_before(self, key, data):
        node = self.find_node_by_key(key)
        if not node:
            return
        new_node = Node(data)
        node.previous.next = new_node
        new_node.previous = node.previous
        new_node.next = node

    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            tail_node = self.tail_node()
            new_node.previous = tail_node
            tail_node.next = new_node

    def bulk_append(self, data_list):
        for data in data_list:
            self.append(data)

    def prepend(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def is_empty(self):
        return not self.head

    def as_list(self):
        node_list = []
        current_node = self.head
        while current_node:
            node_list.append(current_node)
            current_node = current_node.next
        return node_list

    def tail_node(self):
        if self.is_empty():
            return None
        return self.as_list()[-1]

    def find_node_by_key(self, data):
        if self.is_empty():
            return None
        for node in self.as_list():
            if node.data == data:
                return node
        return None

    def __str__(self):
        return str([str(node.data) for node in self.as_list()])
