from datastructure.node import Node


class CircularLinkedList:

    def __init__(self):
        self.head = None

    def prepend(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            new_node.next = self.head
        else:
            new_node.next = self.head
            self.tail_node().next = new_node
            self.head = new_node

    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            new_node.next = self.head
        else:
            new_node.next = self.head
            self.tail_node().next = new_node

    def bulk_append(self, data_list):
        for data in data_list:
            self.append(data)

    def as_list(self):
        node_list = []
        current_node = self.head
        while current_node:
            node_list.append(current_node)
            current_node = current_node.next
            if current_node == self.head:
                break
        return node_list

    def list_size(self):
        return len(self.as_list())

    def is_empty(self):
        return self.list_size() == 0

    def tail_node(self):
        if self.is_empty():
            return None
        return self.as_list()[-1]

    def find_node(self, data):
        return [node for node in self.as_list() if node.data == data][0]

    def find_node_by_index(self, index):
        if index < 0 or self.is_empty():
            return None
        list_size = self.list_size()
        if index > list_size - 1:
            return None
        return self.as_list()[index]

    def remove_node_with_data(self, data):
        if self.is_empty():
            return
        node = self.find_node(data)
        if not node:
            return
        if self.head == node:
            self.tail_node().next = self.head.next
            self.head = self.head.next
        current_node = self.head
        while current_node:
            if current_node.next == node:
                current_node.next = node.next
            else:
                current_node = current_node.next
                if current_node == self.head:
                    return

    def remove_node(self, node):
        if self.is_empty():
            return
        if not node:
            return
        if self.head == node:
            self.tail_node().next = self.head.next
            self.head = self.head.next
        current_node = self.head
        while current_node:
            if current_node.next == node:
                current_node.next = node.next
            else:
                current_node = current_node.next
                if current_node == self.head:
                    return

    @classmethod
    def is_circular_linked_list(cls, linked_list):
        tail_node = linked_list.tail_node()
        if not tail_node or not tail_node.next:
            return False
        if tail_node.next == linked_list.head:
            return True

    @classmethod
    def split_list(cls, circular_linked_list):
        if circular_linked_list.is_empty() or circular_linked_list.list_size() == 1:
            return circular_linked_list.head, circular_linked_list.head
        else:
            list_size = circular_linked_list.list_size()
            list_1_size = list_size // 2
            list_1_head = circular_linked_list.head
            list_1_tail = circular_linked_list.find_node_by_index(list_1_size - 1)
            list_2_head = circular_linked_list.find_node_by_index(list_1_size)
            list_2_tail = circular_linked_list.tail_node()
            list_1_tail.next = list_1_head
            list_2_tail.next = list_2_head
            return list_1_head, list_2_head

    @classmethod
    def josephus(cls, circular_linked_list, k):
        if circular_linked_list.is_empty():
            return None
        current_node = circular_linked_list.head
        length = circular_linked_list.list_size()
        while length > 1:
            count = 1
            while count <= k:
                current_node = current_node.next
                count = count + 1
            circular_linked_list.remove_node(current_node)
            length = circular_linked_list.list_size()

    def __str__(self):
        return str([str(node.data) for node in self.as_list()])



