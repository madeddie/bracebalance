import unittest
from first import balanced


class TestFirst(unittest.TestCase):

    def test_nobraces(self):
        self.assertEqual(balanced('hello world'), -1)

    def test_balanced(self):
        self.assertEqual(balanced('{{{foo();}}}{}'), -1)

    def test_unbalanced(self):
        self.assertEqual(balanced('{}{foo{}'), 2)

    def test_nonstring(self):
        self.assertEqual(balanced(99), -1)


if __name__ == '__main__':
    unittest.main()
