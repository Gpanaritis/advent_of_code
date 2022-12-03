f = open("data.txt","r")

s = 0

for line in f:
    [a,b] = line.strip().split(" ")
    
    if a == "A":
        if b == "X":
            s += 3
        if b == "Y":
            s += 4
        if b == "Z":
            s += 8
    elif a == "B":
        if b == "X":
            s += 1
        if b == "Y":
            s += 5
        if b == "Z":
            s += 9
    elif a == "C":
        if b == "X":
            s += 2
        if b == "Y":
            s += 6
        if b == "Z":
            s += 7
            
print(s)
