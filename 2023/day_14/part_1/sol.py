arr = []

with open("data.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        arr.append(list(line.strip()))

for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] == 'O':
            last_available = i
            for k in range(i - 1, -1, -1):
                if arr[k][j] == '.':
                    last_available = k
                else:
                    break
            arr[i][j] = '.'
            arr[last_available][j] = 'O'

s = 0
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] == 'O':
            s += len(arr) - i
print(s)