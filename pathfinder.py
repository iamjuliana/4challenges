'''
You wake up one day in a strange land not remembering who you are. 

You meet group of strangers who tells you that you are now trapped in a maze.

Then they tell you the most bewildering phenomenon: every day, the maze changes.

The group has a couple of Maze Tracers who map the maze in the day. At night, 
the Path Finders shall use the map to determine if a path can be foound from one point to another.

"You look rather fit.," the leader of the group says to you. She hands you a map. 

"You are now a Path Finder," she says to you.

You look at the map. You are at position [0, 0] in maze of dimension N x N. [0, 0] is the "top left" of the maze map.

You can only move in one of the four cardinal directions i.e. North, East, South, West. 

Return true if you can reach position [N-1, N-1] or false otherwise.

Empty positions are marked .. Walls are marked W. Start and exit positions are empty in all test cases. 

Though you can't remember anything about yourself, you still know how to code. You decided to code a program to read maps given to you everyday.

A simple map looks like this:

Credit: evk
'''

def path_finder(maze):
    # Change input to a list of list of characters
    # e.g. [ ['.'], ['W'], ['.'],
    #        ['.'], ['W'], ['.'],
    #        ['.'], ['.'], ['.'] ]
    m = list(map(list, maze.split())) 

    max = len(m) - 1

    path = [(0, 0)] # put current position in path (drop breadcrumb on current position)
    r, c = 0, 0     # current position

    while (r, c) != (max, max):
        south_step_exists = r+1 <= max and m[r+1][c] == '.' and (r+1,c) not in path
        east_step_exists  = c+1 <= max and m[r][c+1] == '.' and (r,c+1) not in path
        north_step_exists = r-1 >= 0 and m[r-1][c] == '.' and (r-1,c) not in path
        west_step_exists  = c-1 >= 0 and m[r][c-1] == '.' and (r,c-1) not in path

        if south_step_exists:
            r += 1
            path.append((r, c))
        elif east_step_exists:
            c += 1
            path.append((r, c))
        elif north_step_exists:
            r -= 1
            path.append((r, c))
        elif west_step_exists:
            c -= 1
            path.append((r, c))
        else:
            try:
                m[r][c]= 'D'
                row, col = path.pop()
            except:
                # when path.pop() fails i.e. no other step exists
                return False

    return True
