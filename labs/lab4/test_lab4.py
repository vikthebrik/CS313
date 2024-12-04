from rb_tree import Node, rb_tree
import unittest
 
class T0_tree_left_rotation(unittest.TestCase):
    """
    Unit tests for verifying the left rotation functionality of the Red-Black Tree.

    Methods:
        test_tree_left_rotation_1: Tests left rotation on a simple tree with three nodes.
        test_tree_left_rotation_2: Tests left rotation on a larger tree with multiple nodes.
        test_tree_left_rotation_3: Tests left rotation on a specific subtree of a larger tree.
        test_tree_left_rotation_4: Tests left rotation with negative numbers and color validity checks.
    """
    def test_tree_left_rotation_1(self):
        """
        Tests a left rotation on a tree with three nodes.

        Scenario:
        - Inserts 2, 1, 3 into the tree.
        - Rotates the tree about the root node.
        - Asserts that the preorder traversal matches the expected result.
        """
        print("\n")
        print("tree_left_rotation 1")
        tree = rb_tree()
        tree.bst_insert(2)
        tree.bst_insert(1)
        tree.bst_insert(3)
        tree.print_tree()
        print("intial prorder tree", "\n")
        tree.left_rotate(tree.root)
        tree_preorder = [node.data for node in tree.preorder()]
        self.assertEqual(tree_preorder, [3,2,1])
        tree.print_tree()
        print("tree after left rotation about root in prorder")
        print("\n")
    
    def test_tree_left_rotation_2(self):
        """
        Tests a left rotation on a tree with multiple nodes.

        Scenario:
        - Inserts several nodes to create a tree with depth.
        - Rotates the tree about the root node.
        - Asserts that the preorder traversal matches the expected result.
        """
        print("\n")
        print("tree_left_rotation 2")
        tree = rb_tree()
        tree.bst_insert(7)
        tree.bst_insert(5)
        tree.bst_insert(9)
        tree.bst_insert(3)
        tree.bst_insert(6)
        tree.bst_insert(8)
        tree.bst_insert(10)
        tree.bst_insert(1)
        tree.bst_insert(2)
        tree.print_tree()
        print("intial prorder tree", "\n")
        tree.left_rotate(tree.root)
        tree_preorder = [node.data for node in tree.preorder()]
        self.assertEqual(tree_preorder, [9,7,5,3,1,2,6,8,10])
        tree.print_tree()
        print("tree after left rotation about root in prorder")
        print("\n")
    #required test 1 complete in left rot 3
    def test_tree_left_rotation_3(self):
        """
        Tests a left rotation on a specific subtree.

        Scenario:
        - Inserts nodes to form a tree.
        - Rotates the subtree about a specific node.
        - Asserts that the preorder traversal matches the expected result.
        """
        print("\n")
        print("tree_left_rotation 3")
        tree = rb_tree()
        tree.bst_insert(7)
        tree.bst_insert(5)
        tree.bst_insert(9)
        tree.bst_insert(3)
        tree.bst_insert(6)
        tree.bst_insert(8)
        tree.bst_insert(10)
        tree.bst_insert(1)
        tree.bst_insert(2)
        tree.print_tree()
        print("intial prorder tree", "\n")
        tree.left_rotate(tree.find_node(9))
        tree_preorder = [node.data for node in tree.preorder()]
        self.assertEqual(tree_preorder, [7,5,3,1,2,6,10,9,8])
        tree.print_tree()
        print("tree after left rotation about node 9 in prorder")
        print("\n")

    #self test 2, checking negative numbers validity and left rot around root node
    #also checking colors
    def test_tree_left_rotation_4(self):
        """
        Tests a left rotation on a tree with negative numbers.

        Scenario:
        - Inserts negative numbers into the tree.
        - Rotates the tree about the root node.
        - Asserts both preorder traversal and node color validity.
        """
        print("\n")
        print("tree_left_rotation 4")
        tree = rb_tree()
        tree.bst_insert(-7)
        tree.bst_insert(-5)
        tree.bst_insert(-9)
        tree.bst_insert(-3)
        tree.bst_insert(-6)
        tree.bst_insert(-8)
        tree.bst_insert(-10)
        tree.bst_insert(-1)
        tree.bst_insert(-2)
        tree.print_tree()
        print("intial prorder tree", "\n")
        tree.left_rotate(tree.root)
        tree_preorder = [node.data for node in tree.preorder()]
        self.assertEqual(tree_preorder, [-5, -7, -9, -10, -8, -6, -3, -1, -2])
        tree.print_tree()
        print("tree after left rotation about node 9 in prorder")
        print("\n")    

class T1_tree_right_rotation(unittest.TestCase):
    """
    Unit tests for verifying the right rotation functionality of the Red-Black Tree.

    Methods:
        test_tree_right_rotation_1: Tests right rotation on a simple tree with three nodes.
        test_tree_right_rotation_2: Tests right rotation on a larger tree with multiple nodes.
        test_tree_right_rotation_3: Tests right rotation on a specific subtree.
        test_tree_right_rotation_4: Tests right rotation with a large range of numbers.
    """
    def test_tree_right_rotation_1(self):
        """
        Tests a right rotation on a tree with three nodes.

        Scenario:
        - Inserts 2, 1, 3 into the tree.
        - Rotates the tree about the root node.
        - Asserts that the preorder traversal matches the expected result.
        """
        print("\n")
        print("tree_right_rotation 1")
        tree = rb_tree()
        tree.bst_insert(2)
        tree.bst_insert(1)
        tree.bst_insert(3)

        tree.print_tree()
        print("intial prorder tree", "\n")
        tree.right_rotate(tree.root)
        tree_preorder = [node.data for node in tree.preorder()]
        self.assertEqual(tree_preorder, [1,2,3])
        tree.print_tree()
        print("tree after right rotation about root in prorder")
        print("\n")
    
    def test_tree_right_rotation_2(self):
        """
        Tests a right rotation on a tree with multiple nodes.

        Scenario:
        - Inserts several nodes to create a complex tree structure.
        - Rotates the tree about the root node.
        - Asserts that the preorder traversal matches the expected result.
        """
        print("\n")
        print("tree_right_rotation 2")
        tree = rb_tree()
        tree.bst_insert(7)
        tree.bst_insert(5)
        tree.bst_insert(9)
        tree.bst_insert(3)
        tree.bst_insert(6)
        tree.bst_insert(8)
        tree.bst_insert(10)
        tree.bst_insert(1)
        tree.bst_insert(2)
        tree.print_tree()
        print("intial prorder tree", "\n")
        tree.right_rotate(tree.root)
        tree_preorder = [node.data for node in tree.preorder()]
        self.assertEqual(tree_preorder, [5,3,1,2,7,6,9,8,10])
        tree.print_tree()
        print("tree after right rotation about root in prorder")
        print("\n")
    
    #unique test 1 checking preorder after right rotation
    # (replicating the given left rot 3 test on the right rotation)
    def test_tree_right_rotation_3(self):
        """
        Tests a right rotation on a specific subtree.

        Scenario:
        - Inserts nodes to form a tree.
        - Rotates a subtree about a specific node.
        - Asserts that the preorder traversal matches the expected result.
        """
        print("\n")
        print("tree_right_rotation 3")
        tree = rb_tree()
        tree.bst_insert(7)
        tree.bst_insert(5)
        tree.bst_insert(9)
        tree.bst_insert(3)
        tree.bst_insert(6)
        tree.bst_insert(8)
        tree.bst_insert(10)
        tree.bst_insert(1)
        tree.bst_insert(2)
        tree.print_tree()
        print("intial prorder tree", "\n")
        tree.right_rotate(tree.find_node(9))
        tree_preorder = [node.data for node in tree.preorder()]
        self.assertEqual(tree_preorder, [7,5,3,1,2,6,8,9,10])
        
        tree.print_tree()
        print("tree after right rotation about node 9 in prorder")
        print("\n")

    #Self test 3 testing more and larger numbers
    def test_tree_right_rotation_4(self):
        """
        Tests a right rotation on a tree with a larger range of numbers.

        Scenario:
        - Inserts 20 sequentially increasing numbers into the tree.
        - Rotates the tree about the root node.
        - Asserts the preorder traversal after rotation.
        """
        print("\n")
        print("tree_right_rotation 4")
        tree = rb_tree()
        for i in range(20):
            tree.bst_insert(10 * i)
        tree.print_tree()
        print("intial prorder tree", "\n")
        tree.left_rotate(tree.root)
        tree_preorder = [node.data for node in tree.preorder()]
        self.assertEqual(tree_preorder, [10, 0, 20, 30, 40, 50, 60, 70, 
        80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190])
        
        tree.print_tree()
        print("tree after right rotation about node 9 in prorder")
        print("\n")

class T2_tree_insert_color(unittest.TestCase):
    """
    Unit tests for verifying insertion and color properties in the Red-Black Tree.

    Methods:
        test_tree_insert_color_1: Checks the color validity after inserting a small number of nodes.
        test_tree_insert_color_2: Verifies tree balancing and color properties with sequential inserts.
        test_tree_insert_color_3: Tests insertion and color properties on a larger tree.
    """
    def test_tree_insert_color_1(self):
        """
        Checks color properties after inserting four nodes.

        Scenario:
        - Inserts 2, 1, 3, 4 into the tree.
        - Validates preorder traversal and node colors.
        """
        print("\n")
        print("tree_color_check 1")
        
        tree = rb_tree()

        tree.insert(2)
        tree.insert(1)
        tree.insert(3)
        tree.insert(4)
        tree.print_tree()
        tree_preorder = [node.data for node in tree.preorder()]
        tree_preorder_color = [node.color for node in tree.preorder()]
        self.assertEqual(tree_preorder, [2, 1, 3, 4])
        self.assertEqual(tree_preorder_color, ['black', 'black', 'black', 'red'])
        print("\n")

    def test_tree_insert_color_2(self):
        """
        Verifies tree balancing and color properties with sequential inserts.

        Scenario:
        - Inserts values 1 through 7.
        - Checks the tree structure and color assignments in preorder.
        """
        print("\n")
        print("tree_color_check 2")
        
        tree = rb_tree()

        for i in range(1, 8):
            tree.insert(i)
        tree.print_tree()
        tree_preorder = [node.data for node in tree.preorder()]
        tree_preorder_color = [node.color for node in tree.preorder()]
        self.assertEqual(tree_preorder, [2, 1, 4, 3, 6, 5, 7])
        self.assertEqual(tree_preorder_color, ['black', 'black', 'red', 'black', 'black', 'red', 'red'])
        print("\n")

    #required test 2, checking color of inserted values
    def test_tree_insert_color_3(self):
        """
        Tests color properties with a larger tree.

        Scenario:
        - Inserts nodes to form a complex tree.
        - Validates the structure and node colors after insertion.
        """
        print("\n")
        print("tree_color_check")
        
        tree = rb_tree()
        tree.insert(7)
        tree.insert(5)
        tree.insert(9)
        tree.insert(3)
        tree.insert(6)
        tree.insert(8)
        tree.insert(10)
        tree.insert(1)
        tree.insert(2)
        
        tree.print_tree()

        tree_preorder = [node.data for node in tree.preorder()]
        tree_preorder_color = [node.color for node in tree.preorder()]
        self.assertEqual(tree_preorder, [7, 5, 2, 1, 3, 6, 9, 8, 10])
        self.assertEqual(tree_preorder_color, ['black', 'red', 'black', 'red', 'red', 'black', 'black', 'red', 'red'])
        print("\n")

class T3_tree_delete(unittest.TestCase):
    """
    Unit tests for verifying the delete operation in the Red-Black Tree.

    Methods:
        test_tree_delete_0: Tests basic deletion and its impact on tree traversal orders.
        test_tree_delete_1: Verifies the deletion of multiple nodes in sequence.
        test_tree_delete_color_2: Tests the impact of deletion on tree color properties.
    """

    def test_tree_delete_0(self):
        """
        Tests basic deletion on a small tree.

        Scenario:
        - Inserts a few nodes into the tree.
        - Deletes one node and validates preorder traversal and node colors.
        """
        print("\n")
        print("tree_delete test 0")
        print("checking in order, preorder and post order")
        tree = rb_tree()

        tree.insert(7)
        tree.insert(5)
        tree.insert(9)
        tree.insert(6)
        tree_preorder = [node.data for node in tree.preorder()]
        tree_preorder_color = [node.color for node in tree.preorder()]
        self.assertEqual(tree_preorder, [7, 5, 6, 9])
        self.assertEqual(tree_preorder_color, ['black', 'black', 'red', 'black'])
        tree.delete(9)
        tree_preorder = [node.data for node in tree.preorder()]
        tree_preorder_color = [node.color for node in tree.preorder()]
        self.assertEqual(tree_preorder, [6, 5, 7])
        self.assertEqual(tree_preorder_color, ['black', 'black', 'black'])
        print("\n")

    def test_tree_delete_1(self):
        """
        Verifies the deletion of multiple nodes in sequence.

        Scenario:
        - Inserts values 1 through 7.
        - Deletes nodes 5 and 4.
        - Validates preorder traversal and node colors.
        """
        print("\n")
        print("tree_delete 1")
        print("checking in order, preorder and post order")
        tree = rb_tree()

        for i in range(1, 8):
            tree.insert(i)
        tree.delete(5)
        tree.delete(4)
        # tree.print_tree()
        tree_preorder = [node.data for node in tree.preorder()]
        tree_preorder_color = [node.color for node in tree.preorder()]
        self.assertEqual(tree_preorder, [2, 1, 6, 3, 7])
        self.assertEqual(tree_preorder_color, ['black', 'black', 'red', 'black', 'black'])
        print("\n")
    
    def test_tree_delete_color_2(self):
        """
        Tests deletion impact on tree color properties.

        Scenario:
        - Inserts nodes to form a complex tree.
        - Deletes specific nodes and validates both structure and colors in preorder.
        """    
        print("\n")
        print("tree_delete 2")
        tree = rb_tree()
        tree.insert(7)
        tree.insert(5)
        tree.insert(9)
        tree.insert(3)
        tree.insert(6)
        tree.insert(8)
        tree.insert(10)
        tree.insert(1)
        tree.insert(2)
        tree_preorder = [node.data for node in tree.preorder()]
        tree_preorder_color = [node.color for node in tree.preorder()]
        self.assertEqual(tree_preorder, [7, 5, 2, 1, 3, 6, 9, 8, 10])
        self.assertEqual(tree_preorder_color, ['black', 'red', 'black', 'red', 'red', 'black', 'black', 'red', 'red'])
        tree.delete(6)
        tree_preorder = [node.data for node in tree.preorder()]
        tree_preorder_color = [node.color for node in tree.preorder()]
        self.assertEqual(tree_preorder, [7, 2, 1, 5, 3, 9, 8, 10])
        self.assertEqual(tree_preorder_color, ['black', 'red', 'black', 'black', 'red', 'black', 'red', 'red'])
        tree.delete(7)
        tree_preorder = [node.data for node in tree.preorder()]
        tree_preorder_color = [node.color for node in tree.preorder()]
        self.assertEqual(tree_preorder, [8, 2, 1, 5, 3, 9, 10])
        self.assertEqual(tree_preorder_color, ['black', 'red', 'black', 'black', 'red', 'black', 'red'])
        print("\n")


if __name__ == "__main__":
    unittest.main()