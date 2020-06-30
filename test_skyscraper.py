'''
Run this file to test your implementation.
Add additional test cases as needed.
'''

import unittest
from skyscraper import solve_puzzle

class Test(unittest.TestCase):

    def test_skyscraper(self):

        clues = (
            ( 2, 2, 1, 3,  
              2, 2, 3, 1,  
              1, 2, 2, 3,  
              3, 2, 1, 3 ),
            ( 0, 0, 1, 2,   
              0, 2, 0, 0,   
              0, 3, 0, 0, 
              0, 1, 0, 0 ),
            ( 3, 2, 1, 4,
              0, 0, 0, 0,
              0, 0, 0, 0, 
              0, 0, 0, 0 ),
            ( 3, 3, 2, 0, 
              1, 2, 3, 0,    
              0, 0, 1, 0,   
              2, 1, 2, 4 ),
            ( 2, 4, 0, 0,
              1, 2, 4, 0, 
              0, 3, 1, 0, 
              2, 0, 3, 0 ),
            ( 2, 0, 0, 1, 
              0, 3, 0, 0,
              3, 2, 0, 0, 
              0, 3, 2, 0 ),
            ( 3, 0, 0, 0, 
              3, 0, 0, 0, 
              2, 1, 3, 0, 
              3, 1, 0, 0 ),
            ( 0, 3, 0, 0, 
              0, 1, 0, 4, 
              0, 0, 0, 1, 
              0, 2, 2, 0 ),
            ( 3, 2, 1, 2, 
              2, 1, 2, 3, 
              3, 2, 1, 2, 
              2, 1, 2, 3 ),
            ( 0, 0, 0, 0, 
              1, 2, 2, 3, 
              4, 2, 1, 3, 
              0, 0, 0, 0 )
        )

        outcomes = (
            ( ( 1, 3, 4, 2 ),       
              ( 4, 2, 1, 3 ),       
              ( 3, 4, 2, 1 ),
              ( 2, 1, 3, 4 ) ),
            ( ( 2, 1, 4, 3 ), 
              ( 3, 4, 1, 2 ), 
              ( 4, 2, 3, 1 ), 
              ( 1, 3, 2, 4 ) ),
            ( ( 2, 3, 4, 1 ), 
              ( 3, 4, 1, 2 ), 
              ( 4, 1, 2, 3 ), 
              ( 1, 2, 3, 4 ) ),
            ( (1, 2, 3, 4), 
              (2, 1, 4, 3), 
              (4, 3, 1, 2), 
              (3, 4, 2, 1)),
            ( (2, 1, 3, 4), 
              (1, 2, 4, 3), 
              (4, 3, 2, 1), 
              (3, 4, 1, 2) ),
            ( (3, 1, 2, 4), 
              (2, 4, 3, 1), 
              (1, 2, 4, 3), 
              (4, 3, 1, 2)),
            ( (2, 4, 3, 1), 
              (3, 1, 2, 4), 
              (4, 3, 1, 2), 
              (1, 2, 4, 3)),
            ( (2, 1, 4, 3), 
              (3, 2, 1, 4), 
              (1, 4, 3, 2), 
              (4, 3, 2, 1)),
            ( (2, 3, 4, 1), 
              (3, 2, 1, 4), 
              (4, 1, 2, 3), 
              (1, 4, 3, 2)),
            ( (1, 3, 2, 4), 
              (4, 2, 1, 3), 
              (3, 1, 4, 2), 
              (2, 4, 3, 1))
            )

        
        self.assertEqual(solve_puzzle(clues[0]), outcomes[0])
        self.assertEqual(solve_puzzle(clues[1]), outcomes[1])
        self.assertEqual(solve_puzzle(clues[2]), outcomes[2])
        self.assertEqual(solve_puzzle(clues[3]), outcomes[3])
        self.assertEqual(solve_puzzle(clues[4]), outcomes[4])
        self.assertEqual(solve_puzzle(clues[5]), outcomes[5])
        self.assertEqual(solve_puzzle(clues[6]), outcomes[6])
        self.assertEqual(solve_puzzle(clues[7]), outcomes[7])
        self.assertEqual(solve_puzzle(clues[8]), outcomes[8])
        self.assertEqual(solve_puzzle(clues[9]), outcomes[9])
        


unittest.main()

