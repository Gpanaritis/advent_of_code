with open('data.txt', 'r') as f:
    lines = f.readlines()

pipe_map = list(map(lambda x: list(x.strip()), lines))
letter_to_draw = {'|': [(0,1),(1,1),(2,1)], '-':[(1,0),(1,1),(1,2)], 'L':[(0,1),(1,1),(1,2)], 'J':[(0,1),(1,1),(1,0)], '7':[(1,0),(1,1),(2,1)], 'F':[(1,2),(1,1),(2,1)], '.':[], 'S': [(0,1),(1,0),(1,1),(1,2),(2,1)]}

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
def bfs2(start):
    global new_pipe_map

    queue = []
    curr = start
    new_pipe_map[curr[0]][curr[1]] = 2

    for i in {-1, 0 , 1}:
        for j in {-1, 0, 1}:
            if (i == 0 or j == 0) and i != j and 0<=curr[0]+i<len(new_pipe_map) and 0<=curr[1]+j<len(new_pipe_map[0]) and new_pipe_map[curr[0] + i][curr[1] + j] == 0:
                queue.append((curr[0] + i, curr[1] + j))
    
    countee = 0
    while queue:
        curr = queue.pop()
        new_pipe_map[curr[0]][curr[1]] = 2
        for i in {-1, 0 , 1}:
            for j in {-1, 0, 1}:
                if (i == 0 or j == 0) and i != j and 0<=curr[0]+i<len(new_pipe_map) and 0<=curr[1]+j<len(new_pipe_map[0]) and new_pipe_map[curr[0] + i][curr[1] + j] == 0:
                    queue.append((curr[0] + i, curr[1] + j))
        



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
    first = t

    while curr != start:
        prev, curr = curr, get_next(prev, curr)
        loop.append(prev)
        s += 1
    last = prev
    break

for i in range(len(pipe_map)):
    for j in range(len(pipe_map[0])):
        if pipe_map[i][j] != '.' and (i, j) not in loop:
            pipe_map[i][j] = '.'


# x = (first[0] - last[0], first[1] - last[1])
# if first[0] == last[0]:
#     pipe_map[start[0]][start[1]] = '|'
# elif first[1] == last[1]:
#     pipe_map[start[0]][start[1]] = '-'
# elif x == (-1, 1):
#     pipe_map[start[0]][start[1]] = 'J'
# elif x == (1, 1):
#     pipe_map[start[0]][start[1]] = 'L'
# elif x == (1, -1):
#     pipe_map[start[0]][start[1]] = 'F'
# elif x == (-1, -1):
#     pipe_map[start[0]][start[1]] = '7'
# elif first[0] < last[0] and first[1] < last[1]:
#     pipe_map[start[0]][start[1]] = 'L'
# elif first[0] < last[0] and first[1] > last[1]:
#     pipe_map[start[0]][start[1]] = 'F'
# elif first[0] > last[0] and first[1] > last[1]:
#     pipe_map[start[0]][start[1]] = '7'
# elif first[0] > last[0] and first[1] < last[1]:
#     pipe_map[start[0]][start[1]] = 'J'

# print('\n'.join(map(lambda x: ''.join(x), pipe_map)))

new_pipe_map = [[0 for _ in range(len(pipe_map[0]) * 3)] for _ in range(len(pipe_map) * 3)]


# print (new_pipe_map

for i in range(len(pipe_map)):
    for j in range(len(pipe_map[0])):
        for k in letter_to_draw[pipe_map[i][j]]:
            new_pipe_map[i * 3 + k[0]][j * 3 + k[1]] = 1

for i in range(len(new_pipe_map)):
    for j in range(len(new_pipe_map[0])):
        if new_pipe_map[i][j] == 0 and i in {0, len(new_pipe_map) - 1} and j in {0, len(new_pipe_map[0]) - 1}:
            bfs2((i, j))

# reconstruct the new_pipe_map
res = [[0 for _ in range(len(pipe_map[0]))] for _ in range(len(pipe_map))]

for i in range(len(new_pipe_map)):
    for j in range(len(new_pipe_map[0])):
        if new_pipe_map[i][j] == 2 or new_pipe_map[i][j] == 1:
            res[i//3][j//3] = 1

# print 0 count in res
print(sum(map(lambda x: x.count(0), res)))