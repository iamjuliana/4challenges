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


def count_ones_brute(left, right):
    count = 0
    for num in range(left, right+1):
        count += bin(num).count('1')
        # print(f'{bin(num)[2:]:0>30s} - {num:6d} - {count}')
    return count
