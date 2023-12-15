space = []

with open('data.txt', 'r') as f:
    lines = f.readlines()

    for line in lines:
        space.append(list(line.strip()))

def find_min_distances(grid, rows_with_no_galaxies=[], cols_with_no_galaxies=[], space_length=2):
    space_length -= 1
    hash_positions = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '#':
                hash_positions.append((i, j))

    min_distances = []
    for i in range(len(hash_positions)):
        for j in range(i + 1, len(hash_positions)):
            
            # Find how many rows and columns with no galaxies are between the two galaxies
            rows_between = 0
            cols_between = 0

            dist_i = (min(hash_positions[i][0], hash_positions[j][0]), max(hash_positions[i][0], hash_positions[j][0]))
            dist_j = (min(hash_positions[i][1], hash_positions[j][1]), max(hash_positions[i][1], hash_positions[j][1]))

            for row in range(dist_i[0] + 1, dist_i[1]):
                if row in rows_with_no_galaxies:
                    rows_between += 1
            for col in range(dist_j[0] + 1, dist_j[1]):
                if col in cols_with_no_galaxies:
                    cols_between += 1
            
            distance = abs(hash_positions[i][0] - hash_positions[j][0]) + abs(hash_positions[i][1] - hash_positions[j][1]) + rows_between * space_length + cols_between * space_length
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

print(sum(find_min_distances(space, rows_with_no_galaxies, cols_with_no_galaxies, 1000000)))