from datastructure.stack.stack import Stack

if __name__ == '__main__':
    stack = Stack()
    print(stack)
    print(stack.is_empty())
    stack.push("A")
    stack.push("B")
    stack.push("C")
    print(stack)
    print(stack.peek())
    print(stack)
    print(stack.pop())
    print(stack)
    print(stack.is_empty())
