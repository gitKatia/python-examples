from datastructure.doublylinkedlist.doublylinkedlist import DoublyLinkedList

if __name__ == '__main__':
    doubly_linked_list = DoublyLinkedList()
    print(doubly_linked_list)
    doubly_linked_list.bulk_append(["A", "B", "C", "D", "E", "F"])
    print(doubly_linked_list)