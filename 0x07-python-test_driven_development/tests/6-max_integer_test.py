#!/usr/bin/python3
""" Unittest for max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """unittests class for max_integer([])"""
    def test_module_documentation(self):
        """Check for module documentation"""
        m = __import__('6-max_integer').__doc__
        self.assertGreater(len(m), 1)

    def test_function_documentation(self):
        """Cheeck for function documentation"""
        f = max_integer.__doc__
        self.assertTrue((len(f) > 1), 1)

    def test_ordered_list(self):
        """Test with an ordered list"""
        l = [1, 2, 3, 4, 5]
        self.assertEqual(max_integer(l), 5)
    
if __name__ == '__main__':
    unittest.main()
