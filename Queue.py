'''
Queue Implementation in Python
The Queue is built with Linked List
'''

# Node Class to store data

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return str(self.data)

# Queue Class

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # Enqueue Method
    def enqueue(self, data):
        # Create a new node
        new_node = Node(data)

        # Two case to consider
        if self.tail:
            self.tail.next = new_node
        else:
            self.head = new_node

        self.tail = new_node
        self.size += 1

    # Dequeue Method
    def dequeue(self):
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
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(queue.peek())
    print(queue.dequeue())
    print(queue.is_empty())
    print(queue)