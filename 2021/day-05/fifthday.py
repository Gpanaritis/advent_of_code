import numpy as np

class complex:
    def __init__(self,a1,a2):
        self.x = int(a1)
        self.y = int(a2)
    
    @classmethod
    def from_str(cls,str):
        nums = str.split(',')
        return cls(int(nums[0]),int(nums[1]))

    def __repr__(self):
        return f"[{self.x},{self.y}]"

class complexes:
    def __init__(self,str):
        str = str.split(" -> ")
        self.comp = [complex.from_str(str[0]),complex.from_str(str[1])]
        self.dx = self.comp[1].x - self.comp[0].x
        self.dy = self.comp[1].y - self.comp[0].y
    
    def max_y(self):
        return max(node.y for node in self.comp)

    def max_x(self):
        return max(node.x for node in self.comp)

    def __repr__(self):
        return f"[{self.comp[0]},{self.comp[1]}]"


def distance(arr,comp):
    if comp.dx == 0:
        if comp.dy > 0:
            for i in range(comp.comp[0].y ,comp.comp[1].y+1):
                arr[i][comp.comp[0].x] += 1
        if comp.dy < 0:
            for i in range(comp.comp[1].y ,comp.comp[0].y+1):
                arr[i][comp.comp[0].x] += 1
    elif comp.dy == 0:
        if comp.dx > 0:
            for i in range(comp.comp[0].x ,comp.comp[1].x+1):
                arr[comp.comp[0].y][i] += 1
        if comp.dx < 0:
            for i in range(comp.comp[1].x ,comp.comp[0].x+1):
                arr[comp.comp[0].y][i] += 1
    elif abs(comp.dx) == abs(comp.dy):
        if np.sign(comp.dx) ==  np.sign(comp.dy):
            if comp.dx > 0:
                for i in range(0,comp.dx+1):
                    arr[comp.comp[0].y+i][comp.comp[0].x+i] += 1
            if comp.dx < 0:
                for i in range(0,abs(comp.dx)+1):
                    arr[comp.comp[1].y+i][comp.comp[1].x+i] += 1
        if np.sign(comp.dx) !=  np.sign(comp.dy):
            if comp.dx > 0:
                for i in range(0,comp.dx+1):
                    arr[comp.comp[0].y-i][comp.comp[0].x+i] += 1
            if comp.dx < 0:
                for i in range(0,abs(comp.dx)+1):
                    arr[comp.comp[1].y-i][comp.comp[1].x+i] += 1

def max_complex(boxes):
    return max(max(node_2.x for node_2 in node.comp) for node in boxes),max(max(node_2.y for node_2 in node.comp) for node in boxes)
   #return max(node.max_y for node in boxes)

given_file = open('input.txt', 'r')

lines = given_file.readlines()

given_file.close()

boxes = []

for line in lines:
    boxes.append(complexes(line))


max_x,max_y = max_complex(boxes)

arr = [[0 for i in range(max_x+1)] for j in range(max_y+1)]
'''
for box in boxes:
    distance(arr,box)

#print(np.matrix(arr))

p2 = np.asarray(arr)
za = (p2 > 1).sum()

print(za)
print(np.sign(2))
'''

for box in boxes:
    distance(arr,box)

p2 = np.asarray(arr)
za = (p2 > 1).sum()
print(za)