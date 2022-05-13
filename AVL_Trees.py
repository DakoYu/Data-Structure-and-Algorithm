'''
AVL Tree Implementation
'''

# Node Class

class Node:
    def __init__(self, data, parent):
        self.data = data
        self.left = None
        self.right = None
        self.parent = parent
        self.height = 0

# AVL Class

class AVL_Tree:
    def __init__(self):
        self.root = None

    # Insert Method
    def insert(self, data):
        if not self.root:
            self.root = Node(data, None)
        else:
            self.insert_helper(self.root, data)

    def insert_helper(self, node, data):
        # Two case to consider when inserting a node
        if data < node.data:
            if not node.left:
                node.left = Node(data, node)
                node.height = max(self.calc_height(node.left), self.calc_height(node.right))
            else:
                self.insert_helper(node.left , data)
        else:
            if not node.right:
                node.right = Node(data, node)
                node.height = max(self.calc_height(node.left), self.calc_height(node.right))
            else:
                self.insert_helper(node.right , data)

        # Check if the tree is balanced
        self.handle_violation(node)

    # Remove Method
    def remove(self, data):
        if self.root:
            self.remove_helper(self.root, data)

    def remove_helper(self, node, data):
        # Base Case
        # Empty Node
        if not node:
            return
        
        if data < node.data:
            self.remove_helper(node.left, data)
        elif data > node.data:
            self.remove_helper(node.right, data)
        else:
            # Case 1: Leaf Node
            if not node.left and not node.right:
                parent_node = node.parent
                if not node.left and parent_node.left == node:
                    parent_node.left = None
                elif not node.right and parent_node.right == Node:
                    parent_node.right = None

                if not parent_node:
                    self.root = None
                
                del node

                self.handle_violation(node)
            # Case 2: One child
            elif not node.left and node.right:
                parent_node = node.parent
                if parent_node:
                    if parent_node.left == node:
                        parent_node.left = node.left
                    if parent_node.right == node:
                        parent_node.right = node.right
                else:
                    self.root = node.right
                node.right.parent = parent_node
                del node
                self.handle_violation(node)
            elif not node.right and node.left:
                parent_node = node.parent
                if parent_node:
                    if parent_node.left == node:
                        parent_node.left = node.left
                    if parent_node.right == node:
                        parent_node.right = node.right
                else:
                    self.root = node.right
                node.left.parent = parent_node
                del node
                self.handle_violation(node)
            else:
                predecessor = self.get_predecessor(node.left)

                temp = predecessor.data
                predecessor.data = node.data
                node.data = temp

                self.remove_helper(data, predecessor)

    def get_predecessor(self, node):
        if node.right:
            return self.get_predecessor(node.right)
        
        return node

    def calc_height(self, node):
        # Base Case 
        if not node:
            return -1

        return node.height

    def handle_violation(self, node):
        while node:
            node.height = max(self.calc_height(node.left), self.calc_height(node.right)) + 1
            self.violation_helper(node)
            node = node.parent

    def violation_helper(self, node):
        balance = self.calculate_balance(node)
        if balance > 1:
            if self.calculate_balance(node.left) < 0:
                self.rotate_left(node.left)
            self.rotate_right(node)
        if balance < -1:
            if self.calculate_balance(node.right) > 0:
                self.rotate_right(node.right)
            self.rotate_left(node)

    def calculate_balance(self, node):
        if not node:
            return 0

        return self.calc_height(node.left) - self.calc_height(node.right)   

    def rotate_right(self, node):
        print("Rotating to the right on node ", node.data)

        temp_left_node = node.left_node
        t = temp_left_node.right_node

        temp_left_node.right_node = node
        node.left_node = t

        if t is not None:
            t.parent = node

        temp_parent = node.parent
        node.parent = temp_left_node
        temp_left_node.parent = temp_parent

        if temp_left_node.parent is not None and temp_left_node.parent.left_node == node:
            temp_left_node.parent.left_node = temp_left_node

        if temp_left_node.parent is not None and temp_left_node.parent.right_node == node:
            temp_left_node.parent.right_node = temp_left_node

        if node == self.root:
            self.root = temp_left_node

        node.height = max(self.calculate_height(node.left_node), self.calculate_height(node.right_node)) + 1
        temp_left_node.height = max(self.calculate_height(temp_left_node.left_node),
                                    self.calculate_height(temp_left_node.right_node)) + 1

    def rotate_left(self, node):
        print("Rotating to the left on node ", node.data)

        temp_right_node = node.right_node
        t = temp_right_node.left_node

        temp_right_node.left_node = node
        node.right_node = t

        if t is not None:
            t.parent = node

        temp_parent = node.parent
        node.parent = temp_right_node
        temp_right_node.parent = temp_parent

        if temp_right_node.parent is not None and temp_right_node.parent.left_node == node:
            temp_right_node.parent.left_node = temp_right_node

        if temp_right_node.parent is not None and temp_right_node.parent.right_node == node:
            temp_right_node.parent.right_node = temp_right_node

        if node == self.root:
            self.root = temp_right_node

        node.height = max(self.calculate_height(node.left_node), self.calculate_height(node.right_node)) + 1
        temp_right_node.height = max(self.calculate_height(temp_right_node.left_node),
                                     self.calculate_height(temp_right_node.right_node)) + 1     
            


