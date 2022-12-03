f = open("data.txt","r")

s = 0
all = []
for line in f:
    if line.strip() == "":
        all.append(s)
        s = 0
    else:
        s += int(line)



all.sort(reverse = True)

print(all[0] + all[1] + all[2])
