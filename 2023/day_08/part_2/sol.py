from math import lcm

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

# cur pos is all keys in places
cur_pos = [x for x in places.keys() if x[-1] == 'A']
s = [0] * len(cur_pos)

for i in range(len(cur_pos)):
    while cur_pos[i][-1] != 'Z':
        cur_pos[i] = places[cur_pos[i]][moves[s[i]%len(moves)]]
        s[i] += 1
print(lcm(*s))
