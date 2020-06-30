'''
Run this file to test your implementation.
Add additional test cases as needed.
'''

import unittest
from ones import count_ones

class Test(unittest.TestCase):

    def test_ones(self):
        self.assertEqual(count_ones(5,7), 7)
        self.assertEqual(count_ones(12,29), 51)
        self.assertEqual(count_ones(7,17), 26)
        self.assertEqual(count_ones(88483, 7451247), 83376777)
        self.assertEqual(count_ones(25635, 856857476), 12566159299)
        self.assertEqual(count_ones(968, 200000000000000), 4712825299381669)

unittest.main()