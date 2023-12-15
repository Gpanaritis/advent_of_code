space = []

with open('data.txt', 'r') as f:
    lines = f.readlines()

    for line in lines:
        space.append(list(line.strip()))

def find_min_distances(grid):
    hash_positions = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '#':
                hash_positions.append((i, j))

    min_distances = []
    for i in range(len(hash_positions)):
        for j in range(i + 1, len(hash_positions)):
            distance = abs(hash_positions[i][0] - hash_positions[j][0]) + abs(hash_positions[i][1] - hash_positions[j][1])
            min_distances.append(distance)

    return min_distances
    
# find columns and rows that have no # in them
rows_with_no_galaxies = []
cols_with_no_galaxies = []

for i in range(len(space)):
    if '#' not in space[i]:
        rows_with_no_galaxies.append(i)
for i in range(len(space[0])):
    if '#' not in [row[i] for row in space]:
        cols_with_no_galaxies.append(i)

for i in range(len(rows_with_no_galaxies)):
    space.insert(rows_with_no_galaxies[i], ['.' for _ in range(len(space[0]))])
    for j in range(i+1, len(rows_with_no_galaxies)):
        rows_with_no_galaxies[j] += 1

for i in range(len(cols_with_no_galaxies)):
    for row in space:
        row.insert(cols_with_no_galaxies[i], '.')
    for j in range(i+1, len(cols_with_no_galaxies)):
        cols_with_no_galaxies[j] += 1

print(sum(find_min_distances(space)))