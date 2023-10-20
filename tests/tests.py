import unittest
from src.lab3 import BinaryTree, is_tree_balanced


class TestBinaryTree(unittest.TestCase):
    def test_balanced_tree(self):
        root_balanced = BinaryTree(1)
        root_balanced.left = BinaryTree(2)
        root_balanced.right = BinaryTree(3)
        root_balanced.left.left = BinaryTree(4)
        root_balanced.left.right = BinaryTree(5)
        self.assertTrue(is_tree_balanced(root_balanced))

    def test_unbalanced_tree(self):
        root_unbalanced = BinaryTree(1)
        root_unbalanced.left = BinaryTree(2)
        root_unbalanced.right = BinaryTree(3)
        root_unbalanced.left.left = BinaryTree(4)
        root_unbalanced.left.left.left = BinaryTree(5)
        self.assertFalse(is_tree_balanced(root_unbalanced))

    def test_empty_tree(self):
        empty_tree = None
        self.assertTrue(is_tree_balanced(empty_tree))

    def test_single_node_tree(self):
        single_node_tree = BinaryTree(1)
        self.assertTrue(is_tree_balanced(single_node_tree))


if __name__ == '__main__':
    unittest.main()
