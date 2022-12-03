f = open("data.txt","r")

s = 0

for line in f:
    [a,b] = line.strip().split(" ")
    
    if a == "A":
        if b == "X":
            s += 4
        if b == "Y":
            s += 8
        if b == "Z":
            s += 3
    elif a == "B":
        if b == "X":
            s += 1
        if b == "Y":
            s += 5
        if b == "Z":
            s += 9
    elif a == "C":
        if b == "X":
            s += 7
        if b == "Y":
            s += 2
        if b == "Z":
            s += 6
            
print(s)
