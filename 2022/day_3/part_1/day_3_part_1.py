f = open("data.txt", "r")

sum = 0

for line in f:
    a = line[:len(line)//2]
    b = line[len(line)//2:]

    #intersection
    c = set(a).intersection(set(b))


    for i in c:
        if i.islower():
            sum = sum + ord(i) - 96
        elif i.isupper():
            sum += ord(i) - 38

print(sum)