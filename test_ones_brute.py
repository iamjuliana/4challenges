'''
Run this file to test your implementation.
Add additional test cases as needed.
'''

import unittest
from ones_brute import count_ones_brute

class Test(unittest.TestCase):

    def test_brute(self):
        self.assertEqual(count_ones_brute(5,7), 7)
        self.assertEqual(count_ones_brute(12,29), 51)
        self.assertEqual(count_ones_brute(7,17), 26)
        self.assertEqual(count_ones_brute(88483, 7451247), 83376777)
        self.assertEqual(count_ones_brute(25635, 856857476), 12566159299)
        # self.assertEqual(count_ones_brute(968, 200000000000000), 4712825299381669)

unittest.main()