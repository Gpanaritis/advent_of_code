with open("data.txt", "r") as f:
    lines = f.readlines()

moves = [0 if x == 'L' else 1 for x in lines[0].strip()]
places = {}

for i in range(2,len(lines)):
    line = lines[i].strip().split()
    x = line[0]
    l = line[2].removeprefix('(').removesuffix(',')
    r = line[3].removesuffix(')')
    places[x] = (l,r)

cur_pos = 'AAA'
i = 0

while cur_pos != 'ZZZ':
    cur_pos = places[cur_pos][moves[i%len(moves)]]
    i += 1
print(i)
