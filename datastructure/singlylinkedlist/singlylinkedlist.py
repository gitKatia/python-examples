from datastructure.node import Node


class SinglyLinkedList:

    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            self.tail_node().next = new_node

    def bulk_append(self, data_list):
        for data in data_list:
            self.append(data)

    def prepend(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            new_node.next = self.head.next
            self.head = new_node

    def insert_node_after(self, key, data):
        if self.is_empty():
            return
        node = self.find_node_by_key(key)
        if not node:
            return
        new_node = Node(data)
        new_node.next = node.next
        node.next = new_node

    def insert_node_before(self, key, data):
        if self.is_empty():
            return
        current_node = self.head
        previous_node = None
        new_node = Node(data)
        while current_node:
            if current_node.data == key and self.is_head(current_node):
                new_node.next = current_node
                self.head = new_node
                return
            elif current_node.data == key:
                previous_node.next = new_node
                new_node.next = current_node
                return
            else:
                previous_node = current_node
                current_node = current_node.next

    def delete_node_by_key(self, key):
        if self.is_empty():
            return
        current_node = self.head
        previous_node = None
        while current_node:
            if current_node.data == key and self.is_head(current_node):
                self.head = current_node.next
                return
            elif current_node.data == key:
                previous_node.next = current_node.next
                return
            else:
                previous_node = current_node
                current_node = current_node.next

    def delete_node_by_index(self, index):
        if index < 0 or self.is_empty():
            return
        node_list = self.as_list()
        list_size = len(node_list)
        if index > list_size - 1:
            return
        node = node_list[index]
        if self.is_head(node):
            self.head = node.next
        else:
            previous_node = node_list[index - 1]
            previous_node.next = node.next

    def as_list(self):
        node_list = []
        current_node = self.head
        while current_node:
            node_list.append(current_node)
            current_node = current_node.next
        return node_list

    def list_size(self):
        return len(self.as_list())

    def is_empty(self):
        return not self.head

    def is_head(self, node):
        return node == self.head

    def is_tail(self, node):
        return node == self.tail_node()

    def tail_node(self):
        if self.is_empty():
            return None
        return self.as_list()[-1]

    def reverse(self):
        if self.is_empty():
            return
        current_node = self.head
        previous_node = None
        while current_node:
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node
        self.head = previous_node

    def find_node_by_key(self, data):
        if self.is_empty():
            return None
        for node in self.as_list():
            if node.data == data:
                return node
        return None

    def find_previous_by_key(self, key):
        if self.is_empty():
            return None
        current_node = self.head
        previous_node = None
        while current_node:
            if current_node.data == key:
                return previous_node
            previous_node = current_node
            current_node = current_node.next
        return None

    def swap_nodes(self, key1, key2):
        if self.is_empty() or key1 == key2:
            return
        node1 = self.find_node_by_key(key1)
        if not node1:
            return
        node2 = self.find_node_by_key(key2)
        if not node2:
            return
        if node1 == self.head:
            previous_2 = self.find_previous_by_key(key2)
            next_2 = node2.next
            node2.next = node1.next
            self.head = node2
            previous_2.next = node1
            node1.next = next_2
        elif node2 == self.head:
            previous_1 = self.find_previous_by_key(key1)
            next_1 = node1.next
            node1.next = node2.next
            self.head = node1
            previous_1.next = node2
            node2.next = next_1
        else:
            previous_1 = self.find_previous_by_key(key1)
            previous_2 = self.find_previous_by_key(key2)
            next_1 = node1.next
            next_2 = node2.next
            previous_1.next = node2
            previous_2.next = node1
            node2.next = next_1
            node1.next = next_2

    def remove_duplicates(self):
        if self.is_empty():
            return
        current_node = self.head
        data_list = []
        while current_node:
            if current_node.data in data_list:
                self.delete_node_by_key(current_node.data)
            else:
                data_list.append(current_node.data)
            current_node = current_node.next

    def count_occurrences(self, key):
        return len([node for node in self.as_list() if node.data == key])

    def is_palindrome(self):
        if self.is_empty():
            return True
        list_1 = [node.data for node in self.as_list()]
        list_2 = list_1[::-1]
        return list_1 == list_2

    def move_tail_to_head(self):
        if self.is_empty():
            return
        current_node = self.head
        previous_node = None
        while current_node.next:
            previous_node = current_node
            current_node = current_node.next
        previous_node.next = None
        current_node.next = self.head
        self.head = current_node

    def __str__(self):
        return str([str(node.data) for node in self.as_list()])





