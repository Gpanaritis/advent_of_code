from typing import Sized


given_file = open('firstday.txt', 'r')

lines = given_file.readlines()
a = []

for line in lines:
    a.append(int(line))

given_file.close()

sum = 0


for i in range (1,len(a)):
    if a[i]>a[i-1]:
        sum += 1

print(sum)

sum = 0

for i in range (1,len(a)-2):
    if a[i]+a[i+1]+a[i+2] > a[i-1]+a[i]+a[i+1]:
        sum += 1


print(sum)