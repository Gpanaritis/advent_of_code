f = open("data.txt", "r")

cycle = 0
during = 1
after = 1
sum = 0

for line in f:
    line = line.strip()
    line = line.split(" ")

    if line[0] == "noop":
        cycle += 1
        if cycle in {20,60,100,140,180,220}:
            sum += after * cycle

    elif line[0] == "addx":
        cycle += 2
        during = after
        after += int(line[1])
        if cycle in {20,60,100,140,180,220}:
            sum += during * cycle
        elif cycle in {21,61,101,141,181,221}:
            sum += during * (cycle - 1)
print(sum)
