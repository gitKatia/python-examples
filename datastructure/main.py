from datastructure.circularlinkedlist.circularlinkedlist import CircularLinkedList
from datastructure.singlylinkedlist.singlylinkedlist import SinglyLinkedList

if __name__ == '__main__':
    circular_linked_list = CircularLinkedList()
    print(circular_linked_list)
    circular_linked_list.remove_node_with_data("H")
    print("Tail Node:", circular_linked_list.tail_node())
    circular_linked_list.append("A")
    print(circular_linked_list)
    circular_linked_list.append("B")
    print(circular_linked_list)
    print("Tail Node data:", circular_linked_list.tail_node().data)
    circular_linked_list.prepend("0")
    print(circular_linked_list)
    circular_linked_list.remove_node_with_data("0")
    print(circular_linked_list)
    circular_linked_list.bulk_append(["C", "D", "E"])
    print(circular_linked_list)
    CircularLinkedList.josephus(circular_linked_list, 3)
    print(circular_linked_list)
    (a, b) = CircularLinkedList.split_list(circular_linked_list)
    print(a.data)
    print(b.data)
    print(circular_linked_list)
    singly_linked_list = SinglyLinkedList()
    print(CircularLinkedList.is_circular_linked_list(singly_linked_list))
    print(CircularLinkedList.is_circular_linked_list(circular_linked_list))

