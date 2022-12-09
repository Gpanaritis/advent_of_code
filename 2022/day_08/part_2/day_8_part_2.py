f = open("data.txt", "r")

a = []

class tree:
    def __init__(self, value,score):
        self.value = value
        self.score = score

for line in f:
    line = line.strip()
    a.append([])
    for c in line:
        a[-1].append(tree(int(c),1))

for i in range(len(a)):
    for j in range(len(a[0])):
        view = 0
        for k in reversed(range(0,i)):
            l = j
            if a[i][j].value > a[k][l].value:
                view += 1
            elif a[i][j].value <= a[k][l].value:
                view += 1
                break
        if view == 0:
            view = 1
        a[i][j].score *= view

        view = 0
        for k in range(i+1,len(a)):
            l = j
            if a[i][j].value > a[k][l].value:
                view += 1
            elif a[i][j].value <= a[k][l].value:
                view += 1
                break

        if view == 0:
            view = 1
        a[i][j].score *= view

        view = 0
        for l in reversed(range(0,j)):
            k = i
            if a[i][j].value > a[k][l].value:
                view += 1
            elif a[i][j].value <= a[k][l].value:
                view += 1
                break
        if view == 0:
            view = 1
        a[i][j].score *= view
        
        view = 0
        for l in range(j+1,len(a[0])):
            k = i
            if a[i][j].value > a[k][l].value:
                view += 1
            elif a[i][j].value <= a[k][l].value:
                view += 1
                break
        if view == 0:
            view = 1
        a[i][j].score *= view

max = 0
for i in range(1,len(a)-1):
    for j in range(1,len(a[0])-1):
        if a[i][j].score > max:
            print(i,j,a[i][j].score,a[i][j].value)
            max = a[i][j].score
print(max)


