from itertools import repeat

given_file = open('input.txt', 'r')

line = given_file.readline()

given_file.close()

temp = list(map(int,line.split(',')))

lanterfish = list(repeat(0,9))

for t in temp:
    lanterfish[t] += 1

temp = 0

for i in range (0,256):
    temp = lanterfish[0]
    for i in range(1,9):
        lanterfish[i-1] = lanterfish[i]
    lanterfish[6] += temp
    lanterfish[8] = temp

print(sum(lanterfish))