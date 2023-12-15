with open('data.txt') as f:
    lines = f.readlines()

times = list(map(int,lines[0].split(':')[1].strip().split()))
distances = list(map(int,lines[1].split(':')[1].strip().split()))

time = int(''.join(map(str,times)))
distance = int(''.join(map(str,distances)))
s = 0

for i in range(time):
    if i * (time - i) > distance:
        s += 1
print(s)