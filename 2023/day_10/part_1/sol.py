with open('test.txt', 'r') as f:
    lines = f.readlines()

pipe_map = list(map(lambda x: list(x.strip()), lines))

def get_starting_point(pipe_map):
    # Find 'S' in the pipe map
    for i in range(len(pipe_map)):
        for j in range(len(pipe_map[0])):
            if pipe_map[i][j] == 'S':
                return (i, j)

def get_correct(next, momentum):
    if momentum == 'right' and next in {'-', 'J', '7'}:
        return True
    elif momentum == 'left' and next in {'-', 'L', 'F'}:
        return True
    elif momentum == 'up' and next in {'|', 'F', '7'}:
        return True
    elif momentum == 'down' and next in {'|', 'J', 'L'}:
        return True
    else:
        return False

def get_correct_next(next, curr, momentum):
    if next == 'S':
        return True
    # right
    elif curr in {'-', 'L', 'F'} and next in {'-', 'J', '7'} and momentum == (0,1):
        return True
    # left
    elif curr in {'-', 'J', '7'} and next in {'-', 'L', 'F'} and momentum == (0,-1):
        return True
    # up
    elif curr in {'|', 'L', 'J'} and next in {'|', 'F', '7'} and momentum == (1,0):
        return True
    # down
    elif curr in {'|', 'F', '7'} and next in {'|', 'L', 'J'} and momentum == (-1,0):
        return True
    else:
        return False

def get_correct_next_2(next,curr, momentum):
    if next == 'S':
        return True
    if curr == 'L':
        if momentum == (1,0):
            momentum = (0,1)
        elif momentum == (0,-1):
            momentum = (-1,0)
    elif curr == 'J':
        if momentum == (1,0):
            momentum = (0,-1)
        elif momentum == (0,1):
            momentum = (-1,0)
    elif curr == '7':
        if momentum == (-1,0):
            momentum = (0,-1)
        elif momentum == (0,1):
            momentum = (1,0)
    elif curr == 'F':
        if momentum == (-1,0):
            momentum = (0,1)
        elif momentum == (0,-1):
            momentum = (1,0)
    return get_correct_next(next, curr, momentum)

queue = []
to_search = set()
curr = get_starting_point(pipe_map)

for i in {-1, 0 , 1}:
    for j in {-1, 0, 1}:
        if (i == 0 or j == 0) and (i != j):
            queue.append((i, j))

while queue:
    next = queue.pop()
    # print((curr[0] + next[0],curr[1] + next[1]))
    if next == (-1,0) and get_correct(pipe_map[curr[0] + next[0]][curr[1] + next[1]], 'up'):
        to_search.add((curr[0] + next[0], curr[1] + next[1]))
    if next == (1,0) and get_correct(pipe_map[curr[0] + next[0]][curr[1] + next[1]], 'down'):
        to_search.add((curr[0] + next[0], curr[1] + next[1]))
    if next == (0,-1) and get_correct(pipe_map[curr[0] + next[0]][curr[1] + next[1]], 'left'):
        to_search.add((curr[0] + next[0], curr[1] + next[1]))
    if next == (0,1) and get_correct(pipe_map[curr[0] + next[0]][curr[1] + next[1]], 'right'):
        to_search.add((curr[0] + next[0], curr[1] + next[1]))


for t in to_search:
    prev = curr
    curr = t
    s = 0

    while pipe_map[curr[0]][curr[1]] != 'S':

        for i in {-1, 0 , 1}:
            for j in {-1, 0, 1}:
                if (i == 0 or j == 0) and (i != j) and (i,j) != (prev[0] - curr[0], prev[1] - curr[1]) and 0<=curr[0]+i<len(pipe_map) and 0<=curr[1]+j<len(pipe_map[0]) and pipe_map[curr[0] + i][curr[1] + j] != '.':
                    queue.append((i, j))
        
        # print(queue)
        # print(prev)
        
        while queue:
            next = queue.pop()
            next = (curr[0] + next[0], curr[1] + next[1])
            if pipe_map[next[0]][next[1]] == 'S':
                break
            elif not get_correct_next_2(pipe_map[next[0]][next[1]], pipe_map[curr[0]][curr[1]], (curr[0] - prev[0], curr[1] - prev[1])):
                continue
            elif get_correct_next_2(pipe_map[next[0]][next[1]], pipe_map[curr[0]][curr[1]], (curr[0] - prev[0], curr[1] - prev[1])):
                break
        
        s += 1
        prev = curr
        curr = next
        print(curr , pipe_map[curr[0]][curr[1]])
        if s > 3:
            exit()
    break
print((s + 1) // 2)


    




