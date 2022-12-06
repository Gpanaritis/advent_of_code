f = open("data.txt", "r")

count = 0

for line in f:
    line = line.strip()
    for i in range(len(line)):
        a = line[i:i+14]
        #check if duplicates in a
        if len(a) == len(set(a)):
            count = i + 14
            break
    print(count)