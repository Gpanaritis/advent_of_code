from contextlib import suppress

def check_low(arr,i,j):
        list = []
        if i != 0:
            list.append(arr[i-1][j])
        if i != len(arr)-1:
            list.append(arr[i+1][j])
        if j != 0:
            list.append(arr[i][j-1])
        if j != len(arr[0])-1:
            list.append(arr[i][j+1])
        if min(list) <= arr[i][j]:
            return False
        else:
            return True

def generate_basin(basin,arr,i,j):
    if [i,j] not in [j for sub in basins for j in sub] and arr[i][j] != 9 and [i,j] not in basin:
        basin.append([i,j])
        if i!= 0:
            if abs(arr[i][j] - arr[i-1][j]) == 1:
                generate_basin(basin,arr,i-1,j)
        if i != len(arr)-1:
            if abs(arr[i][j] - arr[i+1][j]) == 1:
                generate_basin(basin,arr,i+1,j)
        if j!= 0:
            if abs(arr[i][j] - arr[i][j-1]) == 1:
                generate_basin(basin,arr,i,j-1)
        if j != len(arr[0])-1:
            if abs(arr[i][j] - arr[i][j+1]) == 1:
                generate_basin(basin,arr,i,j+1)

given_file = open('input.txt', 'r')

lines = given_file.readlines()

given_file.close()

arr = [list(map(int, x.replace('\n',''))) for x in lines]
'''
sum = 0
points = 0
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if check_low(arr,i,j):
            points += 1
            sum += 1 + arr[i][j]
print(sum)
print(points)
'''

basins = []
for i in range(len(arr)):
    for j in range(len(arr[i])):
        basin = []
        generate_basin(basin,arr,i,j)
        if basin != []:
            basins.append(basin)

l = [len(x) for x in basins]

l.sort()

p = l[-1]*l[-2]*l[-3]
print(p)

