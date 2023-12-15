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

def main():
    res = []
    x = read_input()
    y = "rn"
    print(hash(y))

if __name__ == "__main__":
    main()