'''
Linked List Implementation in Python
'''

# Node Class to store data and the referrence pointer

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return str(self.data)

    
# Linked List Class to represent the data structure

class Linked_List:
    def __init__(self, head=None):
        # This Linked List contains head and tail pointers
        self.head = head
        self.tail = self.head

    # Insert a new node to the head
    def insert(self, data):
        # Create a new node
        new_node = Node(data)

        # Two case to consider when inserting a new head
        if self.head:
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = self.tail = new_node

    # Remove a node from the head
    def remove(self):
        # Two cse to consider when removing a head
        if self.head:
            delete_node = self.head
            self.head = self.head.next
            return delete_node.data
        else:
            return None
    
    # Append a new to the end of the Linked list
    def append(self, data):
        # Create a new node
        new_node = Node(data)

        # Two case to consider when append a new node
        if self.head:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = self.tail = new_node

    # Remove the last node from the Linked List
    def pop(self):
        # Two case to consider when removing the last node
        if not self.head:
            return None
        else:
            if not self.head.next:
                value = self.head
                self.head = self.tail = None
            else:
                cur = self.head
                while cur.next != self.tail:
                    cur = cur.next
                value = cur.next.data
                cur.next = None
                self.tail = cur
            return value
    
    # Representation of the Linked List
    def __repr__(self):
        output = ''
        cur = self.head
        while cur:
            output += f'{cur} -> '
            cur = cur.next
        return output

l = Linked_List()
l.insert(1)
l.append(2)
l.insert(0)
l.remove()
l.pop()
l.pop()
l.remove()
print(l)
