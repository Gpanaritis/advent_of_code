f = open("data.txt", "r")

a = []

class tree:
    def __init__(self, value,visible):
        self.value = value
        self.visible = visible


for line in f:
    line = line.strip()
    a.append([])
    for c in line:
        a[-1].append(tree(int(c),False))

sum = 0

for i in range(len(a)):
    for j in range(len(a[0])):
        if i == 0:
            a[i][j].visible = True
        elif j == 0:
            a[i][j].visible = True
        elif i == len(a) - 1:
            a[i][j].visible = True
        elif j == len(a[0]) - 1:
            a[i][j].visible = True
        # elif a[i][j-1] < a[i][j] or a[i-1][j] < a[i][j] or a[i][j+1] < a[i][j] or a[i+1][j] < a[i][j]:
        #     print(a[i][j])
        #     sum += 1

for i in range(len(a)):
    max = 0
    for j in range(len(a[0])):
        if(a[i][j].value > max):
            a[i][j].visible = True
            max = a[i][j].value

for i in range(len(a)):
    max = 0
    for j in reversed(range(len(a[0]))):
        if(a[i][j].value > max):
            a[i][j].visible = True
            max = a[i][j].value

for j in range(len(a[0])):
    max = 0
    for i in range(len(a)):
        if(a[i][j].value > max):
            a[i][j].visible = True
            max = a[i][j].value

for j in range(len(a[0])):
    max = 0
    for i in reversed(range(len(a))):
        if(a[i][j].value > max):
            a[i][j].visible = True
            max = a[i][j].value

for i in range(len(a)):
    for j in range(len(a[0])):
        if a[i][j].visible:
            sum += 1

print(sum)