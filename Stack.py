'''
Stack Implementation
The Stack is built on Linked List
'''

# Node class to store the data

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return str(self.data)

# Staack class

class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    # Push Method
    def push(self, data):
        # Create a new node
        new_node = Node(data)

        # Two case to consider
        if self.head:
            new_node.next = self.head

        self.head = new_node
        self.size += 1
    
    # Pop Method
    def pop(self):
        # Two case to consider
        if self.head:
            delete_node = self.head
            self.head = self.head.next
            self.size -= 1
            return delete_node
        return None

    # Is_empty Method
    def is_empty(self):
        return self.size == 0

    # Peek Method
    def peek(self):
        return self.head

    def __repr__(self):
        output = ''
        cur = self.head

        while cur:
            output += f'{cur} -> '
            cur = cur.next
        
        return output

if __name__ == '__main__':
    # Create a new stack
    stack = Stack()
    stack.push(10)
    stack.push(22)
    print(stack.pop())
    print(stack.is_empty())
    print(stack.peek())
    print(stack)