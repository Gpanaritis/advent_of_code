import re

direction = {'up': (-1,0), 'down': (1,0), 'left': (0,-1), 'right': (0,1)}
filename = 'data.txt'

def get_col_size(filename):
    max = 0
    f = open(filename, "r")
    for line in f:
        line = line.rstrip()
        if len(line) == 0:
            break
        if len(line) > max:
            max = len(line)
    f.close()
    return max

def read_file(filename, col_size):
    data = []
    flag = False
    is_first = True
    start_pos = [0,0]

    f = open(filename, "r")

    for line in f:
        line = line.rstrip()
        
        if is_first:
            #find index of first . in line
            start_pos[1] = line.index(".")
            is_first = False

        if len(line) == 0:
            flag = True
            continue

        if not flag:
            data.append([])
            for i in range(col_size):
                if i < len(line):
                    data[-1].append(line[i])
                else:
                    data[-1].append(" ")
        elif flag:
            move = line
            # get all ints from string with regex
            moves = re.findall(r'\d+', move)
            moves = ([int(i) for i in moves], re.findall(r'[A-Z]', move))
            
    return data, moves, start_pos

def change_dir(dir, turn):
    if turn == "L":
        if dir == "up":
            return "left"
        elif dir == "down":
            return "right"
        elif dir == "left":
            return "down"
        elif dir == "right":
            return "up"
    elif turn == "R":
        if dir == "up":
            return "right"
        elif dir == "down":
            return "left"
        elif dir == "left":
            return "up"
        elif dir == "right":
            return "down"

def find_first_by_column(data, col):
    for i in range(len(data)):
        if data[i][col] == ".":
            return i
        elif data[i][col] == "#":
            return -1
    return -1
def find_first_by_row(data, row):
    for i in range(len(data[0])):
        if data[row][i] == ".":
            return i
        elif data[row][i] == "#":
            return -1
    return -1
def find_last_by_column(data, col):
    for i in range(len(data)-1, -1, -1):
        if data[i][col] == ".":
            return i
        elif data[i][col] == "#":
            return -1
    return -1
def find_last_by_row(data, row):
    for i in range(len(data[0])-1, -1, -1):
        if data[row][i] == ".":
            return i
        elif data[row][i] == "#":
            return -1
    return -1


def move(data,pos,dir,number):
    for i in range(number):
        
        if pos[0] + direction[dir][0] < 0:
            k = find_last_by_column(data, pos[1])
            if k != -1:
                new_pos = [k, pos[1]]
            else:
                new_pos = pos
        elif pos[0] + direction[dir][0] >= len(data):
            k = find_first_by_column(data, pos[1])
            if k != -1:
                new_pos = [k, pos[1]]
            else:
                new_pos = pos
        elif pos[1] + direction[dir][1] < 0:
            k = find_last_by_row(data, pos[0])
            if k != -1:
                new_pos = [pos[0], k]
            else:
                new_pos = pos
        elif pos[1] + direction[dir][1] >= len(data[0]):
            k = find_first_by_row(data, pos[0])
            if k != -1:
                new_pos = [pos[0], k]
            else:
                new_pos = pos
        
        else:

            new_pos = [pos[0] + direction[dir][0], pos[1] + direction[dir][1]]

            if data[new_pos[0]][new_pos[1]] == "#":
                break
            elif data[new_pos[0]][new_pos[1]] == " ":
                if dir == "up":
                    k = find_last_by_column(data, pos[1])
                    if k != -1:
                        new_pos = [k, pos[1]]
                    else:
                        new_pos = pos
                elif dir == "down":
                    k = find_first_by_column(data, pos[1])
                    if k != -1:
                        new_pos = [k, pos[1]]
                    else:
                        new_pos = pos
                elif dir == "left":
                    k = find_last_by_row(data, pos[0])
                    if k != -1:
                        new_pos = [pos[0], k]
                    else:
                        new_pos = pos
                elif dir == "right":
                    k = find_first_by_row(data, pos[0])
                    if k != -1:
                        new_pos = [pos[0], k]
                    else:
                        new_pos = pos
            elif data[new_pos[0]][new_pos[1]] == ".":
                pass
        
        pos = new_pos
    return pos

        

a = get_col_size(filename)
data, moves, start_pos = read_file(filename, a)

dir = 'right'
pos = start_pos

pos = move(data, pos, dir, moves[0][0])

for i in range(len(moves[1])):
    dir = change_dir(dir, moves[1][i])
    pos = move(data, pos, dir, moves[0][i+1])

if dir == 'right':
    num = 0
elif dir == 'down':
    num = 1
elif dir == 'left':
    num = 2
elif dir == 'up':
    num = 3

password = 1000 * (pos[0] + 1) + 4 * (pos[1] + 1) + num
print(password)

# print(start_pos, new_pos)