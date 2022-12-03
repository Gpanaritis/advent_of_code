f = open("data.txt","r")

s = 0
all = []
for line in f:
    if line.strip() == "":
        all.append(s)
        s = 0
    else:
        s += int(line)

print(max(all))
