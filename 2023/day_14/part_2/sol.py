import time
arr = []

with open("data.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        arr.append(list(line.strip()))

def find_least_north(O,H, coord):
    i,j = coord
    closest = i
    for k in range(i - 1, -1, -1):
        if (k,j) in H or (k,j) in O:
            O.remove((i,j))
            O.add((closest,j))
            return
        else:
            closest = k
    O.remove((i,j))
    O.add((0,j))
    return

def find_least_south(O,H, coord):
    i,j = coord
    closest = i
    for k in range(i + 1, len(arr)):
        if (k,j) in H or (k,j) in O:
            O.remove((i,j))
            O.add((closest,j))
            return
        else:
            closest = k
    O.remove((i,j))
    O.add((len(arr) - 1,j))
    return

def find_least_east(O,H, coord):
    i,j = coord
    closest = j
    for k in range(j + 1, len(arr[i])):
        if (i,k) in H or (i,k) in O:
            O.remove((i,j))
            O.add((i,closest))
            return
        else:
            closest = k
    O.remove((i,j))
    O.add((i,len(arr[i]) - 1))
    return

def find_least_west(O,H, coord):
    i,j = coord
    closest = j
    for k in range(j - 1, -1, -1):
        if (i,k) in H or (i,k) in O:
            O.remove((i,j))
            O.add((i,closest))
            return
        else:
            closest = k
    O.remove((i,j))
    O.add((i,0))
    return

def tilt_north(O, H):
    sorted_coords = sorted(O, key=lambda coord: (coord[0], coord[1]))
    for coord in sorted_coords:
        find_least_north(O, H, coord)
    return

def tilt_south(O, H):
    sorted_coords = sorted(O, key=lambda coord: (-coord[0], coord[1]))
    for coord in sorted_coords:
        find_least_south(O, H, coord)
    return
    
def tilt_east(O, H):
    sorted_coords = sorted(O, key=lambda coord: (coord[0], -coord[1]))
    for coord in sorted_coords:
        find_least_east(O, H, coord)
    return

def tilt_west(O, H):
    sorted_coords = sorted(O, key=lambda coord: (coord[0], coord[1]))
    for coord in sorted_coords:
        find_least_west(O, H, coord)
    return

O = set()
H = set()
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] == 'O':
            O.add((i,j))
        elif arr[i][j] == '#':
            H.add((i,j))

start = time.time()

s=[]
for _ in range(1000):
    tilt_north(O,H)
    tilt_west(O,H)
    tilt_south(O,H)
    tilt_east(O,H)
    x = 0
    for i,j in O:
        x += len(arr) - i
    s.append(x)

with open('output.txt', 'w') as file:
    for a in s:
        file.write(str(a) + '\n')

end = time.time()

print(end - start)
