f = open("data.txt", "r")

sum = 0

for line in f:
    c = line.split(",")
    a = c[0].split("-")
    b = c[1].split("-")

    a = range(int(a[0]), int(a[1])+1)
    b = range(int(b[0]), int(b[1])+1)

    #check if is overlap
    if set(a).intersection(b):
        sum += 1

print(sum)