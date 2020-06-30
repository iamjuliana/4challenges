'''
You are at position [0, 0] in maze NxN and you can only move in one of the four cardinal directions (i.e. North, East, South, West). Return the minimal number of steps to exit position [N-1, N-1] if it is possible to reach the exit from the starting position. Otherwise, return false in JavaScript/Python and -1 in C++/C#/Java.

Empty positions are marked .. Walls are marked W. Start and exit positions are guaranteed to be empty in all test cases.

Credit: evk
'''

def shortest_path(maze):
    # Change input to a list of list of characters
    # e.g. [ ['.'], ['W'], ['.'],
    #        ['.'], ['W'], ['.'],
    #        ['.'], ['.'], ['.'] ]
    m = list(map(list, maze.split())) 

    max = len(m) - 1

    r, c = 0, 0
    squares = [(r,c)]
    m[r][c] = 0

    while len(squares):
        y, x = squares.pop(0)
        for r, c in (y+1,x), (y,x+1), (y-1,x), (y,x-1):
            if 0 <= r <= max and 0 <= c <= max and m[r][c] == '.':
                m[r][c] = m[y][x] + 1
                squares.append((r,c))
            if r == c == max:
                return m[r][c]

    return False
