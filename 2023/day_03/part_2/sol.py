grid = []

with open('data.txt', 'r') as f:
    for line in f:
        grid.append(list(line.strip()))

def is_adjacent(x, y, grid):
    num_index = []
    for i in range(max(0, x-1), min(len(grid), x+2)):
        for j in range(max(0, y-1), min(len(grid[i]), y+2)):
            if grid[i][j].isnumeric():
                num_index.append((i, j))

    return num_index

gears = []

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == '*':
            gears.append(is_adjacent(i, j, grid))

s = [1] * len(gears)
nums_size = [0] * len(gears)
print(len(gears))
items = [[] for _ in range(len(gears))]
items_index = [[] for _ in range(len(gears))]

num = []
double_break = False
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j].isnumeric():
            num.append((i, j))
        elif num != []:
            for n in num:
                for k in range(len(gears)):
                    if n in gears[k] and num[0] not in items_index[k]:
                        n = int(''.join([grid[x][y] for x,y in num]))
                        s[k] *= n
                        nums_size[k] += 1
                        items_index[k].append(num[0])
            num = []

sum_gears = [s[i] for i in range(len(s)) if nums_size[i] == 2]
print(sum(sum_gears))
