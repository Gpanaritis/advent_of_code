with open('data.txt') as f:
    lines = f.readlines()

times = list(map(int,lines[0].split(':')[1].strip().split()))
distances = list(map(int,lines[1].split(':')[1].strip().split()))

p = 1

for i in range(len(times)):
    s = 0
    for j in range(times[i]):
        if j * (times[i] - j) > distances[i]:
            s += 1
    p *= s
print(p)