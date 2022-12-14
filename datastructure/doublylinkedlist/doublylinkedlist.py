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
        new_node.previous = node
        node.next = new_node

    def add_node_before(self, key, data):
        node = self.find_node_by_key(key)
        if not node:
            return
        new_node = Node(data)
        previous_node = node.previous
        new_node.previous = previous_node
        new_node.next = node
        previous_node.next = new_node
        node.previous = new_node

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

    def delete_node_by_key(self, key):
        node = self.find_node_by_key(key)
        if not node:
            return
        if node == self.head:
            self.head = node.next
            node.next.previous = None
        elif node == self.tail_node():
            previous_node = node.previous
            previous_node.next = None
        else:
            previous_node = node.previous
            previous_node.next = node.next
            node.next.previous = previous_node

    def delete_node(self, node):
        if not node or not self.head:
            return
        if node == self.head:
            self.head = node.next
            node.next.previous = None
        elif node == self.tail_node():
            previous_node = node.previous
            previous_node.next = None
        else:
            previous_node = node.previous
            previous_node.next = node.next
            node.next.previous = previous_node

    def reverse(self):
        if self.is_empty():
            return
        for node in self.as_list():
            previous_node = node.previous
            next_node = node.next
            node.next = previous_node
            node.previous = next_node
        self.head = node

    def remove_duplicates(self):
        if self.is_empty():
            return
        data_list = []
        for node in self.as_list():
            data = node.data
            if data in data_list:
                self.delete_node(node)
            else:
                data_list.append(data)

    @staticmethod
    def pairs_with_sum(linked_list, sum_val):
        if linked_list.is_empty():
            return []
        current_node = linked_list.head
        res_list = []
        while current_node:
            linked_list.update_list(current_node, res_list, sum_val)
            current_node = current_node.next
        return res_list

    @staticmethod
    def update_list(current_node, res_list, sum_val):
        data = current_node.data
        while current_node:
            data_next = current_node.data
            if data + data_next == sum_val:
                res_list.append("(" + str(data) + "," + str(data_next) + ")")
            current_node = current_node.next

    def __str__(self):
        return str([str(node.data) for node in self.as_list()])
