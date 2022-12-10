class position:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def update_position(self, h, v):
        self.x += h
        self.y += v
    
    def distance(self, other):
        return self.x - other.x,self.y - other.y
    
    def follow_head(self,other,flag):
        [x,y] = other.distance(self)

        if x == 2 and y == 0:
            self.update_position(1, 0)
        elif x == -2 and y == 0:
            self.update_position(-1, 0)
        elif x == 0 and y == 2:
            self.update_position(0, 1)
        elif x == 0 and y == -2:
            self.update_position(0, -1)
        elif x == 1 and y == 2:
            self.update_position(1, 1)
        elif x == 1 and y == -2:
            self.update_position(1, -1)
        elif x == -1 and y == 2:
            self.update_position(-1, 1)
        elif x == -1 and y == -2:
            self.update_position(-1, -1)
        elif x == 2 and y == 1:
            self.update_position(1, 1)
        elif x == 2 and y == -1:
            self.update_position(1, -1)
        elif x == -2 and y == 1:
            self.update_position(-1, 1)
        elif x == -2 and y == -1:
            self.update_position(-1, -1)
        elif x == 2 and y == 2:
            self.update_position(1, 1)
        elif x == 2 and y == -2:
            self.update_position(1, -1)
        elif x == -2 and y == 2:
            self.update_position(-1, 1)
        elif x == -2 and y == -2:
            self.update_position(-1, -1)
        
        # if flag:
        #     print(x,y)
        #     print(self.x, self.y)

    
f = open("data.txt", "r")

rope = []

for i in range(10):
    rope.append(position(0,0))

prev = [[0,0]]

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

        rope[0].update_position(h, v)

        for j in range(1,10):
            if rope[4].x == 2 and rope[4].y == 2 and j == 5:
                flag = True
            else:
                flag = False
            rope[j].follow_head(rope[j-1],flag)
        
        # print(H.x, H.y, T.x, T.y)

        if [rope[9].x,rope[9].y] not in prev:
            prev.append([rope[9].x,rope[9].y])
            
# for i in rope:
#     print(i.x, i.y)

print(len(prev))