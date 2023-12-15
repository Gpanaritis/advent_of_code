import sys

def find_refelctive_point(island):
    for i in range(1,len(island)):
        up = island[:i]
        down = island[i:]
        min_len = min(len(up), len(down))
        up = [row for row in up[(len(up) - min_len):]]
        up = up[::-1]
        down = [row for row in down[:min_len]]
        diff_count = 0
        for x, y in zip(up, down):
            for j in range(len(x)):
                if x[j] != y[j]:
                    diff_count += 1
        if diff_count == 1:
            return i * 100

    for i in range(1,len(island[0])):
        left = [row[:i] for row in island]
        right = [row[i:] for row in island]
        min_len = min(len(left[0]), len(right[0]))
        left = [row[(len(left[0]) - min_len):] for row in left]
        left = [row[::-1] for row in left]
        right = [row[:min_len] for row in right]
        diff_count = 0
        for x, y in zip(left, right):
            for j in range(len(x)):
                if x[j] != y[j]:
                    diff_count += 1
        if diff_count == 1:
            return i
    
    return 0


islands = [[],[]]

with open(sys.argv[1], 'r') as f:
    lines = f.readlines()

number_of_islands = 0
islands[0].append([])

for line in lines:
    if line == '\n':
        number_of_islands += 1
        islands[number_of_islands%2].append([])
    else:
        islands[number_of_islands%2][-1].append(list(line.strip()))

s = 0
for i in range(len(islands[0])):
    first_island = islands[0][i]
    second_island = islands[1][i]
    first_reflective_point = find_refelctive_point(first_island)
    second_reflective_point = find_refelctive_point(second_island)
    s += second_reflective_point + first_reflective_point
print(s)