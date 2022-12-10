f = open("data.txt", "r")

def draw(X):
    global crt
    if len(crt) % 40 in {X-1, X, X+1}:
        crt.append('#')
    else:
        crt.append('.')

rows = 6
cols = 40
crt = []

X = 1

for line in f:
    line = line.strip()
    line = line.split(" ")

    if line[0] == "noop":
        draw(X)

    elif line[0] == "addx":
        draw(X)
        draw(X)
        X += int(line[1])

for i in range(rows):
    for j in range(cols):
        print(crt[i*cols + j], end='')
    print()