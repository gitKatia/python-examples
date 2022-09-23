class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:

    def __init__(self):
        self.head = None

    def prepend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            new_node.next = self.head
            self.tail_node().next = new_node
            self.head = new_node

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            new_node.next = self.head
            self.tail_node().next = new_node

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

    def print_list(self):
        node_list = [node.data for node in self.as_list()]
        print(node_list)

    def tail_node(self):
        if not self.head:
            return None
        return self.as_list()[self.list_size() - 1]

    def find_node(self, data):
        return [node for node in self.as_list() if node.data == data][0]

    def find_node_by_index(self, index):
        if index < 0:
            return None
        if not self.head:
            return None
        list_size = self.list_size()
        if index > list_size - 1:
            return None
        return self.as_list()[index]

    def remove_node_with_data(self, data):
        if not self.head:
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
        if not self.head:
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

    def split_list(self):
        if not self.head:
            return self.head, self.head
        else:
            list_size = self.list_size()
            list_1_size = list_size // 2
            list_1_head = self.head
            list_1_tail = self.find_node_by_index(list_1_size - 1)
            list_2_head = self.find_node_by_index(list_1_size)
            list_2_tail = self.tail_node()
            list_1_tail.next = list_1_head
            list_2_tail.next = list_2_head
            return list_1_head, list_2_head


