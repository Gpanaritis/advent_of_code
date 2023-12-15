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

def get_next(prev, curr):
    momentum = (curr[0] - prev[0], curr[1] - prev[1])
    
    if pipe_map[curr[0]][curr[1]] == '-':
        return (curr[0] + momentum[0], curr[1] + momentum[1])
    elif pipe_map[curr[0]][curr[1]] == '|':
        return (curr[0] + momentum[0], curr[1] + momentum[1])
    elif pipe_map[curr[0]][curr[1]] == 'L':
        if momentum == (1,0):
            return (curr[0], curr[1] + 1)
        elif momentum == (0,-1):
            return (curr[0] - 1, curr[1])
    elif pipe_map[curr[0]][curr[1]] == 'J':
        if momentum == (1,0):
            return (curr[0], curr[1] - 1)
        elif momentum == (0,1):
            return (curr[0] - 1, curr[1])
    elif pipe_map[curr[0]][curr[1]] == '7':
        if momentum == (-1,0):
            return (curr[0], curr[1] - 1)
        elif momentum == (0,1):
            return (curr[0] + 1, curr[1])
    elif pipe_map[curr[0]][curr[1]] == 'F':
        if momentum == (-1,0):
            return (curr[0], curr[1] + 1)
        elif momentum == (0,-1):
            return (curr[0] + 1, curr[1])

def bfs(start):
    global pipe_map

    queue = []
    curr = start
    pipe_map[curr[0]][curr[1]] = 'O'

    for i in {-1, 0 , 1}:
        for j in {-1, 0, 1}:
            if (i != 0 and j != 0) and 0<=curr[0]+i<len(pipe_map) and 0<=curr[1]+j<len(pipe_map[0]) and pipe_map[curr[0] + i][curr[1] + j] in {'.', 'X'}:
                queue.append((curr[0] + i, curr[1] + j))
    
    countee = 0
    while queue:
        curr = queue.pop()
        pipe_map[curr[0]][curr[1]] = 'O'
        for i in {-1, 0 , 1}:
            for j in {-1, 0, 1}:
                if (i != 0 and j != 0) and 0<=curr[0]+i<len(pipe_map) and 0<=curr[1]+j<len(pipe_map[0]) and pipe_map[curr[0] + i][curr[1] + j] in {'.', 'X'}:
                    queue.append((curr[0] + i, curr[1] + j))
        # countee += 1
        # if countee > 3:
        #     print(queue)
        #     break
        



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


start = curr
loop = [start]
for t in to_search:
    s = 0
    prev = start
    curr = t

    while curr != start:
        prev, curr = curr, get_next(prev, curr)
        loop.append(prev)
        s += 1
    break

for i in range(len(pipe_map)):
    for j in range(len(pipe_map[0])):
        if pipe_map[i][j] != '.' and (i, j) not in loop:
            pipe_map[i][j] = '.'

for i in range(len(pipe_map)):
    for j in range(len(pipe_map[0])):
        if pipe_map[i][j] == '.' and i in {0, len(pipe_map) - 1} or j in {0, len(pipe_map[0]) - 1}:
            bfs((i, j))

# count dots
count_dots = 0
for i in range(len(pipe_map)):
    for j in range(len(pipe_map[0])):
        if pipe_map[i][j] == '.':
            pipe_map[i][j] = 'I'
            count_dots += 1

for i in range(len(pipe_map)):
    print(''.join(pipe_map[i]))

# print(count_dots)