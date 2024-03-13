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
    def setUp(self):
        self.c1 = Counter()
        self.c2 = Counter()

    def test_singleton(self):
        """Test that all instances are the same object."""
        self.assertIs(self.c1, self.c2)

    def test_share_count(self):
        """Test that all instances share the same count"""
        self.c1.increment()
        self.assertEqual(self.c1.count, self.c2.count)

    def test_no_reset(self):
        """Test is not reset to 0 when you invoke count = Counter() after the first time."""
        self.c1.increment()
        self.assertEqual(self.c1.count, 1)
        c3 = Counter()
        self.assertEqual(c3.count, self.c1.count)
        self.assertEqual(c3.count, 1)