f = open("data.txt", "r")

count = 0
sum = 0
a = []

for line in f:
    a.append(line)
    count += 1

    if count % 3 == 0:
        #intersection of all 3 lines
        c = set(a[0].strip()).intersection(set(a[1])).intersection(set(a[2]))
        
        for i in c:
            if i.islower():
                sum = sum + ord(i) - 96
            elif i.isupper():
                sum += ord(i) - 38

        a = []
print(sum)