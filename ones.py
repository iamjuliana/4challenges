'''
Given two numbers: 'left' and 'right' (1 <= 'left' <= 'right' <= 200,000,000,000,000) return sum of all '1' occurences in binary representations of numbers between 'left' and 'right' (including both)

Example:
count_ones(4, 7) should return 8, because:
4(dec) = 100(bin), which adds 1 to the result.
5(dec) = 101(bin), which adds 2 to the result.
6(dec) = 110(bin), which adds 2 to the result.
7(dec) = 111(bin), which adds 3 to the result.
So finally result equals 8.

Credit: d0n14
'''

from math import log2

def count_ones(left, right):
    if right == 0:
        return 0
    if left == right:
        return bin(left).count('1')
    
    n = int(log2(right))
                  
    part1 = count_ones(1, left-1)   # total 1's from 1 to left-1
    part2 = (n * 2**n) / 2 + 1      # total 1's from 1 to 2**n, where n = floor(log2(right))

    r = right - 2 ** n
    part3 = r + count_ones(1, r)    # total 1's from (2**n + 1) to right

    return int(part2 - part1 + part3)


