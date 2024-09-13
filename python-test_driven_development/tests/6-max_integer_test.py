import unittest
max_integer = __import__('6-max_integer').max_integer


class testmaxinteger(unittest.TestCase):

    def test_max_integer(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_integer(self):
        """Test with a regular list of integers."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_empty_list(self):
        """Test with an empty list."""
        self.assertIsNone(max_integer([]), "Expected None for an empty list")

    def test_single_element(self):
        """Test with a list containing a single element."""
        self.assertEqual(max_integer([5]), 5)

    def test_negative_numbers(self):
        """Test with a list of negative numbers."""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_numbers(self):
        """Test with a list of positive and negative numbers."""
        self.assertEqual(max_integer([1, -2, 3, -4]), 3)


if __name__ == '__main__':
    unittest.main()
