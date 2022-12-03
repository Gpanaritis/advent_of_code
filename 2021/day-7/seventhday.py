from itertools import repeat

given_file = open('input.txt', 'r')

line = given_file.readline()

given_file.close()

arr = list(map(int,line.split(',')))

fuel = [0 for i in range(len(arr))]
fuel_2 = fuel.copy()


for i in range(len(fuel)):
    for j in range(len(arr)):
        fuel[i] += abs(arr[j] - i)

print(min(fuel))



for i in range(len(fuel_2)):
    for j in range(len(arr)):
        fuel_2[i] += (abs(arr[j] - i) + 1) * abs(arr[j] - i) / 2
print(min(fuel_2))