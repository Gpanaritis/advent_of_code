import copy

class position:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def update_position(self, h, v):
        self.x += h
        self.y += v
    
    def distance(self, other):
        return self.x - other.x,self.y - other.y
    
f = open("data.txt", "r")

T = position(0, 0)
H = position(0, 0)

prev = [[T.x,T.y]]

for line in f:
    line = line.strip()
    line = line.split(" ")

    if line[0] == "L":
        h = -1
        v = 0
    elif line[0] == "R":
        h = 1
        v = 0
    elif line[0] == "U":
        h = 0
        v = 1
    elif line[0] == "D":
        h = 0
        v = -1

    for i in range(int(line[1])):

        H.update_position(h, v)

        [x,y] = H.distance(T)

        if x == 2 and y == 0:
            T.update_position(1, 0)
        elif x == -2 and y == 0:
            T.update_position(-1, 0)
        elif x == 0 and y == 2:
            T.update_position(0, 1)
        elif x == 0 and y == -2:
            T.update_position(0, -1)
        elif x == 1 and y == 2:
            T.update_position(1, 1)
        elif x == 1 and y == -2:
            T.update_position(1, -1)
        elif x == -1 and y == 2:
            T.update_position(-1, 1)
        elif x == -1 and y == -2:
            T.update_position(-1, -1)
        elif x == 2 and y == 1:
            T.update_position(1, 1)
        elif x == 2 and y == -1:
            T.update_position(1, -1)
        elif x == -2 and y == 1:
            T.update_position(-1, 1)
        elif x == -2 and y == -1:
            T.update_position(-1, -1)
        
        # print(H.x, H.y, T.x, T.y)

        if [T.x,T.y] not in prev:
            prev.append([T.x,T.y])
            
print(len(prev))


