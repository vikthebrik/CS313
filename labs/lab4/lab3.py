class Node(object):
    """
    Represents a single node in a binary search tree.

    Attributes:
        data (Any): The value stored in the node.
        parent (Node): Reference to the parent node, if any.
        left (Node): Reference to the left child node, if any.
        right (Node): Reference to the right child node, if any.
    """       
   
    def __init__(self, data):
        self.parent = None
        self.left = None
        self.right = None
        self.data = data


class Tree(object):
    """
    A Binary Search Tree (BST) implementation.

    Provides functionality to insert, delete, traverse, and query the tree.

    Attributes:
        root (Node): The root node of the tree, initially set to None.
        PREORDER (int): Constant for preorder traversal.
        INORDER (int): Constant for inorder traversal.
        POSTORDER (int): Constant for postorder traversal.

    Methods:
        insert(data):
            Inserts a new node with the given data into the tree.

        min():
            Returns the minimum value in the tree. Returns None if the tree is empty.

        max():
            Returns the maximum value in the tree. Returns None if the tree is empty.

        contains(data):
            Checks if a node with the given data exists in the tree.

        find_successor(data):
            Finds the successor of the node with the given data.
            Raises:
                KeyError: If the node with the given data does not exist.

        delete(data):
            Deletes the node with the given data from the tree.
            Raises:
                KeyError: If the node with the given data does not exist.

        inorder():
            Performs an inorder traversal and yields the values of the nodes.

        preorder():
            Performs a preorder traversal and yields the values of the nodes.

        postorder():
            Performs a postorder traversal and yields the values of the nodes.

    Errors Raised:
        When using delete if node does not exist
        When using find successor if node does not exist
    """
    # Binary Search Tree
    # class constants
    PREORDER = 1
    INORDER = 2
    POSTORDER = 3

    def __init__(self):
        # Do not create any other private variables.
        # You may create more helper methods as needed.
        self.root = None

    def print(self):
        # Print the data of all nodes in order
        self.__print(self.root)


    def __print(self, curr_node):
        # Recursively print a subtree (in order), rooted at curr_node
        if curr_node is not None:
            self.__print(curr_node.left)
            print(str(curr_node.data), end=' ')  # save space
            self.__print(curr_node.right)
            

    def insert(self, data):
        """
        Inserts a new node with the given data into the tree.
        Param:
            self
            data
        """
        # Find the right spot in the tree for the new node
        # Make sure to check if anything is in the tree
        # Hint: if a node n is None, calling n.data will cause an error
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
            return
        current = self.root
        while current:
            if data < current.data:
                if current.left is None:
                    current.left = new_node
                    new_node.parent = current
                    return
                current = current.left
            else:  # data >= current.data
                if current.right is None:
                    current.right = new_node
                    new_node.parent = current
                    return
                current = current.right

    def min(self):
        """
        Returns the minimum value in the tree. Returns None if the tree is empty.
        Param:
            self
        """
        # Returns the minimum value held in the tree
        # Returns None if the tree is empty
        if self.root is None:
            return None
        current = self.root
        while current.left:
            current = current.left
        return current.data

    def max(self):
        """
        Returns the maximum value in the tree. Returns None if the tree is empty.
        Param:
            self
        """
        # Returns the maximum value held in the tree
        # Returns None if the tree is empty
        if self.root is None:
            return None
        current = self.root
        while current.right:
            current = current.right
        return current.data

    def __find_node(self, data):
        # returns the node with that particular data value else returns None

        current = self.root
        while current:
            if data == current.data:
                return current
            elif data < current.data:
                current = current.left
            else:
                current = current.right
        return None

    def contains(self, data):
        """
        Checks if a node with the given data exists in the tree.
        Param:
            self
            data
        """
        # return True of node containing data is present in the tree.
        # otherwise, return False.
        # you may use a helper method __find_node() to find a particular node with the data value and return that node
        return self.__find_node(data) is not None

    def __iter__(self):
        # iterate over the nodes with inorder traversal using a for loop
        return self.inorder()

    def inorder(self):
        """
        Performs an inorder traversal and yields the values of the nodes.
        Param:
            self
        """
        # inorder traversal : (LEFT, ROOT, RIGHT)
        return self.__traverse(self.root, Tree.INORDER)

    def preorder(self):
        """
        Performs a preorder traversal and yields the values of the nodes.
        Param:
            self
        """
        # preorder traversal : (ROOT, LEFT, RIGHT)
        return self.__traverse(self.root, Tree.PREORDER)

    def postorder(self):
        """
            Performs a postorder traversal and yields the values of the nodes.
            Param:
                self
        """
        # postorder traversal : (LEFT, RIGHT, ROOT)
        return self.__traverse(self.root, Tree.POSTORDER)

    def __traverse(self, curr_node, traversal_type):
        if curr_node is None:
            return
        if traversal_type == Tree.PREORDER:
            yield curr_node.data
            yield from self.__traverse(curr_node.left, traversal_type)
            yield from self.__traverse(curr_node.right, traversal_type)
        elif traversal_type == Tree.INORDER:
            yield from self.__traverse(curr_node.left, traversal_type)
            yield curr_node.data
            yield from self.__traverse(curr_node.right, traversal_type)
        elif traversal_type == Tree.POSTORDER:
            yield from self.__traverse(curr_node.left, traversal_type)
            yield from self.__traverse(curr_node.right, traversal_type)
            yield curr_node.data


    def find_successor(self, data):
        # Find the successor node
        # If the value specified by find_successor does NOT exist in the tree, then raise a KeyError
        # helper method to implement the delete method but may be called on its own
        # If the right subtree of the node is nonempty,then the successor is just 
        # the leftmost node in the right subtree.
        # If the right subtree of the node is empty, then go up the tree until a node that is
        # the left child of its parent is encountered. The parent of the found node will be the
        # successor to the initial node.
        # Note: Make sure to handle the case where the parent is None
    
    	# Return object of successor if found else return None
        node = self.__find_node(data)
        if node is None:
            raise KeyError(f"Node with data {data} not found")
        
        # Case 1: Node has a right subtree
        if node.right:
            successor = node.right
            while successor.left:
                successor = successor.left
            return successor

        # Case 2: No right subtree
        current = node
        while current.parent and current == current.parent.right:
            current = current.parent
        return current.parent

    def delete(self, data):
        # Find the node to delete.
        # If the value specified by delete does NOT exist in the tree, then don't change the tree and raise a KeyError
        # If you find the node and ...
        #  a) The node has no children, just set it's parent's pointer to None.
        #  b) The node has one child, make the nodes parent point to its child.
        #  c) The node has two children, replace it with its successor, and remove
        #       successor from its previous location.
        # Recall: The successor of a node is the left-most node in the node's right subtree.
        # Note: Make sure to handle the case where the parent is None
        node_to_delete = self.__find_node(data)
        if node_to_delete is None:
            raise KeyError(f"Node with data {data} not found")
        
        # Case 1: Node has no children
        if node_to_delete.left is None and node_to_delete.right is None:
            if node_to_delete.parent is None:  # Root node
                self.root = None
            elif node_to_delete == node_to_delete.parent.left:
                node_to_delete.parent.left = None
            else:
                node_to_delete.parent.right = None
        
        # Case 2: Node has one child
        elif node_to_delete.left is None or node_to_delete.right is None:
            child = node_to_delete.left if node_to_delete.left else node_to_delete.right
            if node_to_delete.parent is None:  # Root node
                self.root = child
            elif node_to_delete == node_to_delete.parent.left:
                node_to_delete.parent.left = child
            else:
                node_to_delete.parent.right = child
            child.parent = node_to_delete.parent
        
        # Case 3: Node has two children
        else:
            successor = self.find_successor(data)
            node_to_delete.data = successor.data
            # Remove the successor
            if successor == successor.parent.left:
                successor.parent.left = successor.right
            else:
                successor.parent.right = successor.right
            if successor.right:
                successor.right.parent = successor.parent



