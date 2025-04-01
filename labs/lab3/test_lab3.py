import lab4.lab3 as lab3
import unittest

class TestInsertMethod(unittest.TestCase):
    def test_insert(self):
        t = lab3.Tree()
        t.insert(10)
        t.insert(5)
        t.insert(15)

        self.assertEqual(t.root.data, 10)
        self.assertEqual(t.root.left.data, 5)
        self.assertEqual(t.root.right.data, 15)


class TestTraverseMethod(unittest.TestCase):
    def test_traverse(self):
        t = lab3.Tree()
        t.insert(4)
        t.insert(2)
        t.insert(6)
        t.insert(1)
        t.insert(3)
        t.insert(5)
        t.insert(7)

        inorder = [node for node in t.inorder()]
        preorder = [node for node in t.preorder()]
        postorder = [node for node in t.postorder()]

        self.assertEqual(inorder, [1, 2, 3, 4, 5, 6, 7])
        self.assertEqual(preorder, [4, 2, 1, 3, 6, 5, 7])
        self.assertEqual(postorder, [1, 3, 2, 5, 7, 6, 4])


class TestFindNodeMethod(unittest.TestCase):
    def test_find_node(self):
        t = lab3.Tree()
        t.insert(8)
        t.insert(3)
        t.insert(10)

        node = t._Tree__find_node(10)  # Accessing private method
        self.assertIsNotNone(node)
        self.assertEqual(node.data, 10)

        non_existent_node = t._Tree__find_node(99)
        self.assertIsNone(non_existent_node)


class TestContainsMethod(unittest.TestCase):
    def test_contains(self):
        t = lab3.Tree()
        t.insert(8)
        t.insert(3)
        t.insert(10)

        self.assertTrue(t.contains(8))
        self.assertTrue(t.contains(3))
        self.assertFalse(t.contains(99))


class TestFindSuccessorMethod(unittest.TestCase):
    def test_find_successor(self):
        t = lab3.Tree()
        t.insert(8)
        t.insert(3)
        t.insert(10)
        t.insert(1)
        t.insert(6)
        t.insert(4)
        t.insert(7)

        self.assertEqual(t.find_successor(6).data, 7)
        self.assertEqual(t.find_successor(3).data, 4)
        self.assertEqual(t.find_successor(8).data, 10)

    def test_find_successor_empty_tree(self):
        t = lab3.Tree()
        with self.assertRaises(KeyError):
            t.find_successor(1)


class TestDeleteMethod(unittest.TestCase):
    def test_delete(self):
        t = lab3.Tree()
        t.insert(8)
        t.insert(3)
        t.insert(10)
        t.insert(1)
        t.insert(6)

        t.delete(3)
        self.assertFalse(t.contains(3))

        inorder = [node for node in t]
        self.assertEqual(inorder, [1, 6, 8, 10])

    def test_delete_empty_tree(self):
        t = lab3.Tree()
        with self.assertRaises(KeyError):
            t.delete(1)


if __name__ == '__main__':
    unittest.main()
