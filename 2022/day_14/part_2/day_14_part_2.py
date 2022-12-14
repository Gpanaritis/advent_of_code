import numpy as np

def falling_sand(n):
    try:
        global air, rock, sand
        i = 0
        j = 500
        while True:
            
            if n[i+1,j] == air :
                n[i,j] = air
                n[i+1,j] = sand
                i += 1
            elif n[i+1,j-1] == air:
                n[i,j] = air
                n[i+1,j-1] = sand
                i += 1
                j -= 1
            elif n[i+1,j+1] == air:
                n[i,j] = air
                n[i+1,j+1] = sand
                i += 1
                j += 1
            else:
                return i,j
    except IndexError:
        return 'finished'

f = open('data.txt', 'r')

xmin = 100000
xmax = 0
ymin = 100000
ymax = 0

air = 0
rock = 1
sand = 2

for line in f:
    line = line.strip()
    line = line.split(' -> ')
    a = [s.split(',') for s in line]

    for c in a:
        if int(c[0]) < xmin:
            xmin = int(c[0])
        if int(c[0]) > xmax:
            xmax = int(c[0])
        if int(c[1]) < ymin:
            ymin = int(c[1])
        if int(c[1]) > ymax:
            ymax = int(c[1])

n = np.zeros((ymax + 3, xmax + ymax + 3))

f.close()

f = open('data.txt', 'r')

for line in f:
    line = line.strip()
    line = line.split(' -> ')
    a = [s.split(',') for s in line]
    prev = None

    for c in a:
        if prev is None:
            prev = c
            continue
        elif prev is not None:
            for i in range(min(int(prev[1]), int(c[1])), max(int(prev[1]), int(c[1]))+1):
                for j in range(min(int(prev[0]), int(c[0])), max(int(prev[0]), int(c[0]))+1):
                    n[i, j] = rock
            prev = c
n[ymax + 2, :] = rock
print(n[:,493:])

f.close()

count = 1

s = falling_sand(n)


while s != 'finished' and not (s[0] == 0 and s[1] == 500):
    count += 1
    n[s[0], s[1]] = sand
    s = falling_sand(n)
print(count)


