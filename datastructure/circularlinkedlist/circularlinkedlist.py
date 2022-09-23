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

    def remove_node(self, data):
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


if __name__ == '__main__':
    circular_linked_list = CircularLinkedList()
    circular_linked_list.print_list()
    circular_linked_list.remove_node("H")
    print("Tail Node:", circular_linked_list.tail_node())
    circular_linked_list.append("A")
    circular_linked_list.print_list()
    circular_linked_list.append("B")
    circular_linked_list.print_list()
    print("Tail Node data:", circular_linked_list.tail_node().data)
    circular_linked_list.prepend("0")
    circular_linked_list.print_list()
    circular_linked_list.remove_node("0")
    circular_linked_list.print_list()
    circular_linked_list.append("C")
    circular_linked_list.append("D")
    circular_linked_list.append("E")
    circular_linked_list.print_list()
    (a, b) = circular_linked_list.split_list()
    print(a)
    print(b)

