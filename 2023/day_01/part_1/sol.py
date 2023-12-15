with open('data.txt') as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]

s = 0

first = 0
last = 0

for line in lines:
    for c in line:
        if c.isnumeric():
            first = int(c)
            break
    for c in line[::-1]:
        if c.isnumeric():
            last = int(c)
            break
    # concat first and last
    s += int(str(first) + str(last))

print(s)
