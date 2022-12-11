class Monkey:
    def __init__(self,items,operation,test,iftrue,iffalse):
        self.items = items
        self.operation = operation
        self.test = test
        self.iftrue = iftrue
        self.iffalse = iffalse
        self.count = 0

m = []
old = 0
new = 0
flag = False

#Data
m.append(Monkey([98,89,52],"new = old * 2","flag = (new % 5 == 0)",6,1))
m.append(Monkey([57,95,80,92,57,78],"new = old * 13","flag = (new % 2 == 0)",2,6))
m.append(Monkey([82, 74, 97, 75, 51, 92, 83],"new = old + 5","flag = (new % 19 == 0)",7,5))
m.append(Monkey([97, 88, 51, 68, 76],"new = old + 6","flag = (new % 7 == 0)",0,4))
m.append(Monkey([63],"new = old + 1","flag = (new % 17 == 0)",0,1))
m.append(Monkey([94, 91, 51, 63],"new = old + 4","flag = (new % 13 == 0)",4,3))
m.append(Monkey([61, 54, 94, 71, 74, 68, 98, 83],"new = old + 2","flag = (new % 3 == 0)",2,7))
m.append(Monkey([90, 56],"new = old * old","flag = (new % 11 == 0)",3,5))

#Test
# m.append(Monkey([79, 98],"new = old * 19","flag = (new % 23 == 0)",2,3))
# m.append(Monkey([54, 65, 75, 74],"new = old + 6","flag = (new % 19 == 0)",2,0))
# m.append(Monkey([79, 60, 97],"new = old * old","flag = (new % 13 == 0)",1,3))
# m.append(Monkey([74],"new = old + 3","flag = (new % 17 == 0)",0,1))

for i in range(20):
    for j,monkey in enumerate(m):
        for item in monkey.items:
            old = item
            exec(monkey.operation) # new = old + something
            new = new // 3
            exec(monkey.test)
            if flag:
                m[monkey.iftrue].items.append(new)
            else:
                m[monkey.iffalse].items.append(new)
            m[j].count += 1
        m[j].items = []

c = [monkey.count for monkey in m]
c.sort(reverse=True)
print(c[0] * c[1])