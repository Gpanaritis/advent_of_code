import pandas as pd

data = pd.read_csv('secondday.txt', sep=" ", header=None)

horizontal = 0
depth = 0



for i in range (0,len(data)):
    if str(data[0][i]) == "forward":
        horizontal += data[1][i]
    elif str(data[0][i]) == "down":
        depth += data[1][i]
    elif str(data[0][i]) == "up":
        depth -= data[1][i]

print(horizontal*depth)

horizontal = 0
depth = 0
aim = 0

for i in range (0,len(data)):
    if str(data[0][i]) == "forward":
        horizontal += data[1][i]
        depth += aim * data[1][i]
    elif str(data[0][i]) == "down":
        aim += data[1][i]
    elif str(data[0][i]) == "up":
        aim -= data[1][i]

print(horizontal*depth)