'''
Run this file to check your implementation.
Add additional test cases as needed.
'''

import unittest
from pathfinder import path_finder

class Test(unittest.TestCase):

    def test_pathfinder(self):
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
        e = "\n".join([
        "...W....W....W..W........",
        ".W..W.....W.....W...W....",
        "W...W.W...W..W....W....W.",
        "..W.W....W...WWW..W..W...",
        "..W.WWW..W.....WWWWW....W",
        ".....W..W....W......W..W.",
        "......W.W.......W...W....",
        "..WW.W..W.......W...WWW..",
        "W...W...W.......W...W....",
        ".......W.W....W.....W....",
        "....W........W......W...W",
        ".........WWWWWW..W..W..W.",
        ".....W...W.......W..W....",
        ".W..W.WWWW.......W..W....",
        "W.....W.............W....",
        ".....W..W....W......W..W.",
        "......W.W.......W...W....",
        "..WW.W..W.......W...WWW..",
        "W...W...W.......W...W....",
        ".......W.W....W.....W....",
        "....W........W......W...W",
        ".........WWWWWW..W..W..W.",
        ".....W...W.......W..W....",
        ".W..W.WWWW.......W..W....",
        "W.....W.............W....",

        ])
        f = "\n".join([
        "...WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW...WWWWWWWW.",
        "WW........W.....W...W.......W.......WWWW..........",
        "WW.WWW...W..W....W.............W....W..W.......W..",
        "WW.W....W...WWW..W..W......W....W....W..W.....W...",
        "WW.WWWW..W.....WWWWW......W...W...W....W..WWWW...W",
        ".....W..W....W......W....W....W....W..W........WWW",
        "......W.W.......W...W.......W....W..........W.....",
        "..WW.W............W........WWW.................WW.",
        "W...W...W.......W...W.......W....W....W..W....W...",
        ".......W.W...........W.......W...........W........",
        "....W........W......W...W...W......v..............",
        ".........WWWWWW........W..W..W....W....W.W........",
        ".....W...W.......W..W.................W..W........",
        ".W..W.WWWW.......W..W.......W............W.......W",
        "W.....W.............W.......W....W....W..W........",
        "...WWWW......W...W......W............WW......WWW..",
        "WW........W.....W...W.......W....W....W..W........",
        "WW.WWW...W..W....W....W....W....W....W..W......W..",
        "WW.W....W...WWW..W..W......W....W....W..W.....W...",
        "WW.WWWW..W.....WWWWW....W................W........",
        ".....W..W....W......W....................W........",
        "......W.W.........................W...W...........",
        "..WW.W..W.......W...WWW.....W....W....W..W........",
        "W...W...W.......W...W.............W...............",
        ".......W.W..........W.....W.......................",
        "....W........W......W...W......v..................",
        ".........WWWWWW..W..W..W....W....W....W..W........",
        ".....W...W................................W.......",
        ".W..W.WWWW.......W.......W.......................W",
        "W.....W.............W.......W....W....W..W........",
        "...WWWW..........WW.............................W.",
        "WW........W.....W...W....W........W....W..........",
        "WW.WWW...W..W....W....W....W....W....W..W......W..",
        "WW.W....W...WWW..W..W......W..................W...",
        "WW.WWWW..W.....WWWWW....W...W.....................",
        ".....W..W....W......W..W....W....W....W..W........",
        "......W.W.......W...W......WW....W....W..W........",
        "..WW.W..W.......W...WWW...W...W...................",
        "W...W...W.......W...W...WWW.W....W....W..W......W.",
        ".......W.W....W.....W.WW.........W....W..W...WWW.W",
        "....W........W......W...W...W....W....W..W...W....",
        ".........WWW.............WW.......W....W.....WWW..",
        ".....W...W.......W..W...WW.......W....W..W..WW....",
        ".W..W.WWWW............WW.......W....W..W...W....WW",
        "W.....W.............W.W..........W....W..WWW...W..",
        "....W........W.........W........W....W..W.........",
        ".........W........W..W..W.........W....W..W..W....",
        ".....W...W........W............W....W..WW.W..WW...",
        ".W..W.WWWW.......W..W............W....W..W.WW.W..W",
        "W.....W.............W............W....W..W.W.W....",
        ])

        with open('maze.dat', 'r') as file:
            g = file.read()
        
        self.assertEqual(path_finder(a), True)
        self.assertEqual(path_finder(b), False)
        self.assertEqual(path_finder(c), True)
        self.assertEqual(path_finder(d), False)
        self.assertEqual(path_finder(e), True)
        self.assertEqual(path_finder(f), False)
        self.assertEqual(path_finder(g), True)

unittest.main()