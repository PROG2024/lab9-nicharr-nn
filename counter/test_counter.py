"""Write a unit test to verify that Counter is a singleton.

   Also verify that all instances share the same count
   and that the count is not reset to 0 when you invoke 
   count = Counter() 
   after the first time.

   You can use pytest or unittest.
"""

import unittest
from counter import Counter

class TestCounter(unittest.TestCase):
    def test_singleton(self):
        """Test that all instances are the same object."""
        c1 = Counter()
        c2 = Counter()
        self.assertIs(c1, c2)

    def test_share_count(self):
        """Test that all instances share the same count"""
        c1 = Counter()
        c2 = Counter()
        c1.increment()
        self.assertEqual(c1.count, 1)
        self.assertEqual(c2.count, 1)

    def test_no_reset(self):
        """Test is not reset to 0 when you invoke count = Counter() after the first time."""
        c1 = Counter()
        c1.increment()
        self.assertEqual(c1.count, 1)
        c2 = Counter()
        self.assertEqual(c2.count, c1.count)
        self.assertEqual(c2.count, 1)
