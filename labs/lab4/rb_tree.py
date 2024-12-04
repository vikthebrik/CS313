class Node(object):
    def __init__(self, data, left = None, right = None, parent = None, color = 'red'):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent
        self.color = color

class rb_tree(object):

    PREORDER = 1
    INORDER = 2
    POSTORDER = 3
    # initialize root and size
    def __init__(self):
        self.root = None
        self.sentinel = Node(None, color = 'black')
        self.sentinel.parent = self.sentinel
        self.sentinel.left = self.sentinel
        self.sentinel.right = self.sentinel
    
    def print_tree(self):
        # Print the data of all nodes in order
        self.__print_tree(self.root)
    
    def __print_tree(self, curr_node):
        # Recursively print a subtree (in order), rooted at curr_node
        # Printed in preorder
        if curr_node is not self.sentinel:
            print(str(curr_node.data), end=' ')  # save space
            self.__print_tree(curr_node.left)
            self.__print_tree(curr_node.right)

    def __print_with_colors(self, curr_node):
        # Recursively print a subtree (in order), rooted at curr_node
        # Printed in PREORDER
        # Extracts the color of the node and print it in the format -dataC- where C is B for black and R for red
        if curr_node is not self.sentinel:

            if curr_node.color == "red":
                node_color = "R"
            else:
                node_color = "B"

            print(str(curr_node.data)+node_color, end=' ')  # save space
            self.__print_with_colors(curr_node.left)
            self.__print_with_colors(curr_node.right)

    def print_with_colors(self):
        # Also prints the data of all node but with color indicators
        self.__print_with_colors(self.root)
            
            
    def __iter__(self):
        return self.inorder()

    def inorder(self):
        return self.__traverse(self.root, rb_tree.INORDER)

    def preorder(self):
        return self.__traverse(self.root, rb_tree.PREORDER)

    def postorder(self):
        return self.__traverse(self.root, rb_tree.POSTORDER)

    def __traverse(self, curr_node, traversal_type):
        if curr_node is not self.sentinel:
            if traversal_type == self.PREORDER:
                yield curr_node
            yield from self.__traverse(curr_node.left, traversal_type)
            if traversal_type == self.INORDER:
                yield curr_node
            yield from self.__traverse(curr_node.right, traversal_type)
            if traversal_type == self.POSTORDER:
                yield curr_node

    # find_min travels across the leftChild of every node, and returns the
    # node who has no leftChild. This is the min value of a subtree
    def find_min(self, start_node=None):
        current_node = start_node if start_node else self.root
        while current_node.left is not self.sentinel:
            current_node = current_node.left
        return current_node

    
    # find_node expects a data and returns the Node object for the given data
    def find_node(self, data):
        if self.root:
            res = self.__get(data, self.root)
            if res:
                return res
            else:
                raise KeyError('Error, data not found')
        else:
            raise KeyError('Error, tree has no root')

    # helper function __get receives a data and a node. Returns the node with
    # the given data
    def __get(self, data, current_node):
        if current_node is self.sentinel: # if current_node does not exist return None
            print("couldnt find data: {}".format(data))
            return None
        elif current_node.data == data:
            return current_node
        elif data < current_node.data:
            # recursively call __get with data and current_node's left
            return self.__get( data, current_node.left )
        else: # data is greater than current_node.data
            # recursively call __get with data and current_node's right
            return self.__get( data, current_node.right )
    

    def find_successor(self, data):
        # Private Method, can only be used inside of BST.
        current_node = self.find_node(data)

        if current_node is self.sentinel:
            raise KeyError

        # Travel left down the rightmost subtree
        if current_node.right:
            current_node = current_node.right
            while current_node.left is not self.sentinel:
                current_node = current_node.left
            successor = current_node

        # Travel up until the node is a left child
        else:
            parent = current_node.parent
            while parent is not self.sentinel and current_node is not parent.left:
                current_node = parent
                parent = parent.parent
            successor = parent

        if successor:
            return successor
        else:
            return None

    # put adds a node to the tree
    def insert(self, data):
        # if the tree has a root
        if self.root:
            # use helper method __put to add the new node to the tree
            new_node = self.__put(data, self.root)
            self.__rb_insert_fixup(new_node)
        else: # there is no root
            # make root a Node with values passed to put
            self.root = Node(data, parent = self.sentinel, left = self.sentinel, right = self.sentinel)
            new_node = self.root
            self.__rb_insert_fixup(new_node)
    
    #Insertion for Binary Search Tree
    def bst_insert(self, data):
        # if the tree has a root
        if self.root:
            # use helper method __put to add the new node to the tree
            self.__put(data, self.root)
        else: # there is no root
            # make root a Node with values passed to put
            self.root = Node(data, parent = self.sentinel, left = self.sentinel, right = self.sentinel)
        
    # helper function __put finds the appropriate place to add a node in the tree
    def __put(self, data, current_node):
        if data < current_node.data:
            if current_node.left != self.sentinel:
                new_node = self.__put(data, current_node.left)
            else: # current_node has no child
                new_node = Node(data,
                parent = current_node,
                left = self.sentinel,
                right = self.sentinel )
                current_node.left = new_node
        else: # data is greater than or equal to current_node's data
            if current_node.right != self.sentinel:
                new_node = self.__put(data, current_node.right)
            else: # current_node has no right child
                new_node = Node(data,
                parent = current_node,
                left = self.sentinel,
                right = self.sentinel )
                current_node.right = new_node
        return new_node

    def left_rotate(self, x):
        y = x.right
        if y == self.sentinel:
            raise KeyError("Cannot left rotate without a valid right child.")
        
        # Turn y's left subtree into x's right subtree
        x.right = y.left
        if y.left != self.sentinel:
            y.left.parent = x
        
        # Link y's parent to x's parent
        y.parent = x.parent
        if x.parent == self.sentinel:  # x was root
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        
        # Put x as y's left child
        y.left = x
        x.parent = y

    def right_rotate(self, y):
        x = y.left
        if x == self.sentinel:
            raise KeyError("Cannot right rotate without a valid left child.")
        
        # Turn x's right subtree into y's left subtree
        y.left = x.right
        if x.right != self.sentinel:
            x.right.parent = y
        
        # Link x's parent to y's parent
        x.parent = y.parent
        if y.parent == self.sentinel:  # y was root
            self.root = x
        elif y == y.parent.right:
            y.parent.right = x
        else:
            y.parent.left = x
        
        # Put y as x's right child
        x.right = y
        y.parent = x

    def __rb_insert_fixup(self, z):
        while z.parent.color == "red":  # Parent is red
            if z.parent == z.parent.parent.left:  # Parent is left child
                y = z.parent.parent.right  # Uncle
                if y.color == "red":  # Case 1: Uncle is red
                    z.parent.color = "black"
                    y.color = "black"
                    z.parent.parent.color = "red"
                    z = z.parent.parent  # Move up the tree
                else:
                    if z == z.parent.right:  # Case 2: z is right child
                        z = z.parent
                        self.left_rotate(z)
                    # Case 3: z is left child
                    z.parent.color = "black"
                    z.parent.parent.color = "red"
                    self.right_rotate(z.parent.parent)
            else:  # Symmetric cases for right child
                y = z.parent.parent.left  # Uncle
                if y.color == "red":  # Case 1: Uncle is red
                    z.parent.color = "black"
                    y.color = "black"
                    z.parent.parent.color = "red"
                    z = z.parent.parent  # Move up the tree
                else:
                    if z == z.parent.left:  # Case 2: z is left child
                        z = z.parent
                        self.right_rotate(z)
                    # Case 3: z is right child
                    z.parent.color = "black"
                    z.parent.parent.color = "red"
                    self.left_rotate(z.parent.parent)
        self.root.color = "black"

    def delete(self, data):
        z = self.find_node(data)
        if z == self.sentinel:
            raise KeyError(f"Node with data {data} not found.")
        
        y = z
        y_original_color = y.color
        if z.left == self.sentinel:
            x = z.right
            self.__transplant(z, z.right)
        elif z.right == self.sentinel:
            x = z.left
            self.__transplant(z, z.left)
        else:
            y = self.find_min(start_node=z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.__transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.__transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        
        if y_original_color == "black":
            self.__rb_delete_fixup(x)

    def __rb_delete_fixup(self, x):
        while x != self.root and x.color == "black":
            if x == x.parent.left:
                w = x.parent.right  # Sibling
                if w.color == "red":  # Case 1: Sibling is red
                    w.color = "black"
                    x.parent.color = "red"
                    self.left_rotate(x.parent)
                    w = x.parent.right
                if w.left.color == "black" and w.right.color == "black":  # Case 2: Both children black
                    w.color = "red"
                    x = x.parent
                else:
                    if w.right.color == "black":  # Case 3: Right child black
                        w.left.color = "black"
                        w.color = "red"
                        self.right_rotate(w)
                        w = x.parent.right
                    # Case 4: Right child red
                    w.color = x.parent.color
                    x.parent.color = "black"
                    w.right.color = "black"
                    self.left_rotate(x.parent)
                    x = self.root
            else:  # Symmetric cases for right child
                w = x.parent.left  # Sibling
                if w.color == "red":  # Case 1: Sibling is red
                    w.color = "black"
                    x.parent.color = "red"
                    self.right_rotate(x.parent)
                    w = x.parent.left
                if w.left.color == "black" and w.right.color == "black":  # Case 2: Both children black
                    w.color = "red"
                    x = x.parent
                else:
                    if w.left.color == "black":  # Case 3: Left child black
                        w.right.color = "black"
                        w.color = "red"
                        self.left_rotate(w)
                        w = x.parent.left
                    # Case 4: Left child red
                    w.color = x.parent.color
                    x.parent.color = "black"
                    w.left.color = "black"
                    self.right_rotate(x.parent)
                    x = self.root
        x.color = "black"

    def __transplant(self, u, v):
        if u.parent == self.sentinel:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent