import re
# L is how many crates we got
l = 9

a = []
for i in range(l):
    a.append([])

f = open("data.txt", "r")

flag = False

for line in f:
    #remove the newline character
    b = line.rstrip()

    if not b.strip():
        # print(a)
        continue

    if b.strip()[0].isdigit():
        flag = True
        continue
    
    f = False

    if not flag:
        i = 0
        count = 0
        for c in b:
            if c == ']':
                f = False
            if f:
                a[i].append(c)
                i += 1
            if c == '[':
                count = 0
                f = True
            if c == ' ':
                count += 1
            if not count==0 and count % 4 == 0:
                i += 1


    elif flag:
        #find all numbers
        b = re.findall(r'\d+', b)
        print(b)
        for i in range(int(b[0])):
            c = a[int(b[1])-1].pop(0)
            a[int(b[2])-1].insert(0,c)

#print from a the first element of each list
for i in range(len(a)):
    print(a[i][0],end='')