f = open("data.txt", "r")

sum = 0

for line in f:
    line = line.strip()
    for i in range(len(line)):
        a = line[i:i+4]
        #check if duplicates in a
        if len(a) == len(set(a)):
            sum += i + 4
            break
    

print(sum)