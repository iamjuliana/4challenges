'''
Run this file to test your implementation.
Add additional test cases as needed.
'''

import unittest
from shortest_path import shortest_path

class Test(unittest.TestCase):

    def test_shortestpath(self):
        a = "\n".join([
        ".W.",
        ".W.",
        "..."
        ])

        b = "\n".join([
        ".W.",
        ".W.",
        "W.."
        ])

        c = "\n".join([
        "......",
        "......",
        "......",
        "......",
        "......",
        "......"
        ])

        d = "\n".join([
        "......",
        "......",
        "......",
        "......",
        ".....W",
        "....W."
        ])

        with open('maze.dat', 'r') as file:
            e = file.read()

        self.assertEqual(shortest_path(a), 4)
        self.assertEqual(shortest_path(b), False)
        self.assertEqual(shortest_path(c), 10)
        self.assertEqual(shortest_path(d), False)
        self.assertEqual(shortest_path(e), 306)

unittest.main()