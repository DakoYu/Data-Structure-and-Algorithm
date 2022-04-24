'''
Double Linked List Implementation
'''

# Node Class to store data and reference pointers

class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    def __repr__(self):
        return str(self.data)


# Double Linked List Class

class Double_LinkedList:
    def __init__(self, head=None):
        self.head = None
        self.tail = self.head

    # Assign the head and the tail to the same node
    def _head_tail(self, node):
        self.head = self.tail = node

    # Insert a new node to the head
    def insert(self, data):
        # Create a new node
        new_node = Node(data)

        # Two cases to consider when inserting a new node
        if self.head:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        else:
            self._head_tail(new_node)
    
    # Append a new node to the tail
    def append(self, data):
        # Create a new node
        new_node = Node(data)

        # Two cases to consider when append a new node
        if self.head:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        else:
            self._head_tail(new_node)

    # Remove the head node
    def remove(self):
        # Two case to consider when removing the head
        if self.head:
            delete_node = self.head
            # if there is more than 2 nodes in the DLL
            if self.head.next:
                delete_node.next.prev = None
                self.head = self.head.next
                delete_node.next = None
            else:
                self.head = self.tail = None
            return delete_node
        else:
            return None

    # Retrieve the first node
    def peek(self):
        return self.head

    # Traverse the DLL from tail to head
    def traverse_tail(self):
        output = ''
        cur = self.tail

        while cur:
            output += f'{cur} -> '
            cur = cur.prev
        
        return output


    # Pop the tail node
    def pop(self):
        # Two case to consider when removing the tail
        if self.head:
            delete_node = self.tail
            # if there is more than 2 nodes in the DLL
            if self.head.next:
                self.tail = self.tail.prev
                self.tail.next = None
                delete_node.prev = delete_node.next = None
            else:
                self.head = self.tail = None
            return delete_node
        else:
            return None
    
    def __repr__(self):
        output = ''
        cur = self.head

        while cur:
            output += f'{cur} -> '
            cur = cur.next
        
        return output

if __name__ == '__main__':
    dll = Double_LinkedList()
    dll.insert(1)
    dll.insert(0)
    dll.append(2)
    print(dll.traverse_tail())
    dll.remove()
    print(dll)