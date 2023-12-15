import sys

def read_input():
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()
        for line in lines:
            x = line.strip().split(",")
    
    return x

def hash(x):
    y = 0
    for c in x:
        y += ord(c)
        y *= 17
        y %= 256
    
    return y

def add_to_box(boxes, x):
    y = x.split("=")
    z = hash(y[0])
    if y[0] not in [i[0] for i in boxes[z]]:
        boxes[z].append(y)
    else:
        for i in boxes[z]:
            if i[0] == y[0]:
                i[1] = y[1]
    return boxes

def remove_from_box(boxes, x):
    y = x.split("-")[0]
    z = hash(y)
    boxes[z] = [i for i in boxes[z] if i[0] != y]

    return boxes

def calc_res(boxes):
    s = 0
    for i in range(len(boxes)):
        for j in range(len(boxes[i])):
            s += (i+1) * (j+1) * int(boxes[i][j][1])
    return s


def main():
    res = []
    x = read_input()
    boxes = [[] for _ in range(256)]
    for i in x:
        if '=' in i:
            boxes = add_to_box(boxes, i)
        elif '-' in i:
            boxes = remove_from_box(boxes, i)
    s = calc_res(boxes)
    print(s)

if __name__ == "__main__":
    main()