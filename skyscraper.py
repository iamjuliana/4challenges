'''
In a grid of 4 by 4 squares you want to place a skyscraper in each square with only some clues:

- The height of the skyscrapers is between 1 and 4
- No two skyscrapers in a row or column may have the same number of floors
- A clue is the number of skyscrapers that you can see in a row or column from the outside
- Higher skyscrapers block the view of lower skyscrapers located behind them

Can you write a program that can solve this puzzle?

Example:

To understand how the puzzle works, this is an example of a row with 2 clues. Seen from the left side there are 4 buildings visible while seen from the right side only 1:

   -------------------------
4  |     |     |     |     |  1
   -------------------------

There is only one way in which the skyscrapers can be placed. From left-to-right all four buildings must be visible and no building may hide behind another building:

   -------------------------
4  |  1  |  2  |  3  |  4  |  1
   -------------------------

Example of a 4 by 4 puzzle with the solution:

                  1     2
   -------------------------
   |     |     |     |     |  
   -------------------------
   |     |     |     |     |  2
   -------------------------
1  |     |     |     |     |  
   -------------------------
   |     |     |     |     |  
   -------------------------
                  3




                  1     2
   -------------------------
   |  2  |  1  |  4  |  3  |  
   -------------------------
   |  3  |  4  |  1  |  2  |  2
   -------------------------
1  |  4  |  2  |  3  |  1  |  
   -------------------------
   |  1  |  3  |  2  |  4  |  
   -------------------------
                  3


Your task: complete the solve_puzzle function

Clues are passes in a tuple of 16 items. This tuple contains the clues around the clock index:

      0     1     2     3
   -------------------------
15 |     |     |     |     |  4
   -------------------------
14 |     |     |     |     |  5
   -------------------------
13 |     |     |     |     |  6
   -------------------------
12 |     |     |     |     |  7
   -------------------------
      11    10    9     8

If no clue is available, return '0'
Each puzzle has only one possible solution.
solve_puzzle function returns a tuple fof tuples. The first indexer is for the row, the second indexer for the column. 

Credit: FranKK
'''

from itertools import permutations 
from copy import deepcopy


def is_valid(*args):
   """
   Determines if the given sequences form a valid grid.
   *arg - sequences of same size
   Assumes that each arg is of the same length
   Example:
   (1,2,3,4), (4,2,3,1) -> False, double 3 in col 3
   (1,2,3,4), (4,4,2,1) -> False, double 4 in row 2
   (1,2,3,4), (4,3,2,1) -> True
   """
   for a in args:
      if len(set(a)) != len(a):
         return False 
   
   for a in list(zip(*args)):
      if len(set(a)) != len(a):
         return False 

   return True


def visible(buildings):
   """
   Returns number of visible buildings given a cellection of heights.
   buildings - a sequence of numbers
   Assumes that the 0th index item is in front.
   """
   count, highest_visible = 1, buildings[0]

   for b in buildings[1:]:
      if b > highest_visible:
         count += 1
         highest_visible = b

   return count



def check(clues, sequence):
   """
   Determines if all building sequences given fulfill clue requirements.
   clues - a sequence of clues
   seqeunce - a list of building sequences
   Example:
   clues    : (0,0,1,2)
   building : [[1,2,4,3], 
               [2,1,4,3], 
               [4,3,1,2], 
               [3,2,4,1]]
   Returns True
   Assumes that clues are valid numbers
   """

   for i, building in enumerate(sequence):
      if  clues[i] > 0 and visible(building) != clues[i]:
         return False 
   return True



def generate_grids():
   """
   Generates a list of valid 4x4 grids.
   """
   s = []
   p = list(permutations([1,2,3,4]))
   for first in set(permutations([1,2,3,4])):
      for second in set(permutations([1,2,3,4])):
         if not is_valid(first, second):
            continue
         for third in set(permutations([1,2,3,4])):
            if not is_valid(first, second, third):
               continue  
            for fourth in set(permutations([1,2,3,4])):
               if is_valid(first, second, third, fourth): 
                  s.append(list(map(list,[first, second, third, fourth])))
   return s


candidates = None

def solve_puzzle(clues):
   global candidates

   # reorganise clues
   clues = clues[0:8] + clues[11:7:-1] + clues[15:11:-1]

   candidates = generate_grids()
   clues_fulfilled = False

   while not clues_fulfilled:
      grid = candidates.pop()

      # check against north clues
      north_facing = list(map(list,zip(*grid)))
      north_ok = check(clues[:4], north_facing)

      # check against east clues
      east_facing = deepcopy(grid)
      [_.reverse() for _ in east_facing]
      east_ok = check(clues[4:8], east_facing)
      
      # check against south clues
      south_facing = deepcopy(north_facing)
      [_.reverse() for _ in south_facing]
      south_ok = check(clues[8:12], south_facing)

      # check against west clues
      west_ok = check(clues[12:], grid)

      clues_fulfilled = north_ok and east_ok and south_ok and west_ok

   return tuple(map(tuple,grid))

