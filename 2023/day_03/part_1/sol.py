grid = []

with open('data.txt', 'r') as f:
    for line in f:
        grid.append(list(line.strip()))

def is_adjacent(x, y, grid):
    for i in range(max(0, x-1), min(len(grid), x+2)):
        for j in range(max(0, y-1), min(len(grid[i]), y+2)):
            if grid[i][j] != '.' and not grid[i][j].isnumeric():
                return True

    return False

num = []
s = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j].isnumeric():
            num.append((i, j))
        else:
            for n in num:
                if is_adjacent(n[0], n[1], grid):
                    n = [grid[x][y] for x, y in num]
                    s += int(''.join(n))
                    break
            num = []

print(s)
