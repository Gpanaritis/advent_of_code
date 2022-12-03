given_file = open('thirdday.txt', 'r')

lines = given_file.readlines()
a = []

for line in lines:
    a.append(line)

given_file.close()

s = ""
s_2 = ""
b = a.copy()

while len(a) > 1:
    a.sort()
    c = 0
    for i in range (0,len(a)):
        if a[i][0] == '1':
            c = i
            break
    if c <= len(a)/2:
        del a[:c]
    elif c > len(a)/2:
        del a[c:]
    s += a[0][0]

    for i in range(0,len(a)):
        a[i] = a[i][1:]

print(s+a[0])

while len(b) > 1:
    b.sort()
    c = 0
    for i in range (0,len(b)):
        if b[i][0] == '1':
            c = i
            break
    #print(c)
    if c <= len(b)/2:
        del b[c:]
    elif c > len(b)/2:
        del b[:c]
    s_2 += b[0][0]

    for i in range(0,len(b)):
        b[i] = b[i][1:]


print(s_2+b[0])

o2 = int(s+a[0],2)
co2 = int(s_2+b[0],2)

print(o2,co2)


