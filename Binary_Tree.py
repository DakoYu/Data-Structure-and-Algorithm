'''
Binary Search Tree Implementation
'''

# Node Class

class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.data)


# Binary Search Tree Class

class BST:
    def __init__(self, root=None):
        self.root = None

    # Insert Method
    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self.insert_helper(self.root, data)

    def insert_helper(self, node, data):
        # Base Case: empty node
        if not node:
            return
        
        # Two Case
        # If the data is less then the current node data
        if data < node.data:
            # Consider if there is left child or not
            if node.left:
                self.insert_helper(node.left, data)
            else:
                node.left = Node(data)
        else:
            # Consider if there is right child or not
            if node.right:
                self.insert_helper(node.right, data)
            else:
                node.right = Node(data)

    # Find Method
    def find(self, data):
        return self.find_helper(self.root, data)

    def find_helper(self, node, data):
        # Base Case
        # Empty searched data
        if not node:
            return False

        # Three Case to consider
        if node.data == data:
            return True
        elif data < node.data:
            return self.find_helper(node.left, data)
        else:
            return self.find_helper(node.right, data)

    # Delete Method
    def delete(self, data):
        self.delete_helper(self.root, data)

    def delete_helper(self, node, data):
        # Base Case
        # Empty Node
        if not node:
            return 

        # Assign the pointers accordingly
        if data < node.data:
            node.left = self.delete_helper(node.left, data)
        elif data > node.data:
            node.right = self.delete_helper(node.right, data)
        else:
            # Deleted node is found
            # Deleted node has 0 or 1 child
            if not node.left:
                temp = node.right
                node = None
                return temp
            elif not node.right:
                temp = node.left
                node = None
                return temp
            else:
                # Deleted node has 2 children
                # Find the max node from the left tree
                current_max = self.max(node.left)
                node.data = current_max.data
                node.left = self.delete_helper(node.left, current_max.data)
        return node

    # Min Mehotd
    def min(self, node=None):
        # Iterate through the left node of the tree
        if not node:
            node = self.root
        while node.left:
            node = node.left

        return node

    # Max Method
    def max(self, node=None):
        # Iterate through the right node of the tree
        if not node:
            node = self.root

        while node.right:
            node = node.right
        
        return node

    # Traversal Methods

    # In Order Traversal Method
    def in_order(self):
        return self.in_order_helper(self.root)

    def in_order_helper(self, node):
        # Base Case
        # Empty Node
        if not node:
            return ''
        
        # Left Root Right Recurssion
        return f'{self.in_order_helper(node.left)}{str(node.data)} {self.in_order_helper(node.right)}'

    # Pre Order Traversal Method
    def pre_order(self):
        return self.pre_order_helper(self.root)

    def pre_order_helper(self, node):
        # Base Case 
        # Empty Node
        if not node:
            return ''
        
        # Root Left Right Recurssion
        return f'{node.data} {self.pre_order_helper(node.left)}{self.pre_order_helper(node.right)}'

    # Post Order Traversal Method
    def post_order(self):
        return self.post_order_helper(self.root)

    def post_order_helper(self, node):
        # Base Case
        # Empty Node
        if not node:
            return ''

        # Left Right Root
        return f'{self.post_order_helper(node.left)}{self.post_order_helper(node.right)}{node.data} '

def compare_helper(node1, node2):
    if not node1 or not node2:
        return node1 == node2
    if node1.data is not node2.data:
        return False
    return compare_helper(node1.left, node2.left) and compare_helper(node1.right, node2.right)

def compare(bst1, bst2):
    return compare_helper(bst1.root, bst2.root)




if __name__ == '__main__':
    bst = BST()
    bst.insert(10)
    bst.insert(12)
    bst.insert(8)
    bst.insert(4)
    bst.insert(11)
    bst.insert(15)
    bst.insert(14)
    bst.insert(13)
    # print(bst.min())
    # print(bst.max())
    bst2 = BST()
    bst2.insert(10)
    bst2.insert(12)
    bst2.insert(8)
    bst2.insert(4)
    bst2.insert(11)
    bst2.insert(15)
    bst2.insert(14)
    bst2.insert(13)
    print(compare(bst, bst2))
    # print(bst.delete(12))
    # print(bst.delete(15))
    # print(bst.in_order())
    # print(bst.pre_order())
    # print(bst.post_order())