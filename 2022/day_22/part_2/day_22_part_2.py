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

def find_first_by_column(data, col, i_offset, j_offset):
    col = col % 50
    for i in range(i_offset, i_offset + 50):
        if data[i][col + j_offset] == ".":
            return [i, col + j_offset], 'down'
        elif data[i][col + j_offset] == "#":
            return -1
    return -1
def find_first_by_row(data, row, i_offset, j_offset):
    
    # if print_flag:
    #     print(pos, row)
    row = row % 50
    for j in range(j_offset, j_offset + 50):
        if data[row + i_offset][j] == ".":
            return [row + i_offset, j], 'right'
        elif data[row + i_offset][j] == "#":
            return -1
    return -1
def find_last_by_column(data, col, i_offset, j_offset):
    col = col % 50
    for i in range(i_offset + 49, i_offset - 1, -1):
        if data[i][col + j_offset] == ".":
            return [i, col + j_offset], 'up'
        elif data[i][col + j_offset] == "#":
            return -1
    return -1
def find_last_by_row(data, row, i_offset, j_offset):
    
    row = row % 50
    for j in range(j_offset + 49,j_offset -1, -1):
        if data[row + i_offset][j] == ".":
            
            return [row + i_offset, j], 'left'
        elif data[row + i_offset][j] == "#":
            # print([row + i_offset, j])
            return -1
    return -1





def find_down(data, col,pos):
    if col < 50: # orange to blue
        i_offset = 0
        j_offset = 100
        return find_first_by_column(data, col, i_offset, j_offset)
    elif col < 100: # white to orange
        i_offset = 150
        j_offset = 0
        return find_last_by_row(data, col, i_offset, j_offset)

    elif col < 150: # blue to red
        i_offset = 50
        j_offset = 50
        return find_last_by_row(data, col, i_offset, j_offset)
   
def find_right(data, row):
    if row < 50: #blue to white
        i_offset = 100
        j_offset = 50
        row = 49 - row
        return find_last_by_row(data, row, i_offset, j_offset)
    elif row < 100: #red to blue
        i_offset = 0
        j_offset = 100
        return find_last_by_column(data, row, i_offset, j_offset)
    elif row < 150: #white to blue
        i_offset = 0
        j_offset = 100
        row = 49 - row
        return find_last_by_row(data, row, i_offset, j_offset)
    elif row < 200: #orange to white
        i_offset = 100
        j_offset = 50
        return find_last_by_column(data, row, i_offset, j_offset)

def find_up(data, col):
    if col < 50: #green to red
        i_offset = 50
        j_offset = 50
        return find_first_by_row(data, col, i_offset, j_offset)
    elif col < 100: #yellow to orange
        i_offset = 150
        j_offset = 0
        return find_first_by_row(data, col, i_offset, j_offset)
    elif col < 150: #blue to orange
        i_offset = 150
        j_offset = 0
        return find_last_by_column(data, col, i_offset, j_offset)

def find_left(data, row):

    if row < 50: #yellow to green
        i_offset = 100
        j_offset = 0
        row = 49 - row
        return find_first_by_row(data, row, i_offset, j_offset)
    elif row < 100: #red to green
        i_offset = 100
        j_offset = 0
        return find_first_by_column(data, row, i_offset, j_offset)
    elif row < 150: #green to yellow
        i_offset = 0
        j_offset = 50
        row = 49 - row
        return find_first_by_row(data, row, i_offset, j_offset)
    elif row < 200: #orange to yellow
        i_offset = 0
        j_offset = 50
        return find_first_by_column(data, row, i_offset, j_offset)
    


def move(data,pos,dir,number):
    for i in range(number):
        
        if pos[0] + direction[dir][0] < 0:
            k = find_up(data, pos[1])
            if k != -1:
                new_pos,dir = k
            else:
                new_pos = pos
        elif pos[0] + direction[dir][0] >= len(data):
            k = find_down(data, pos[1], pos)
            if k != -1:
                new_pos,dir = k
            else:
                new_pos = pos
        elif pos[1] + direction[dir][1] < 0:
            k = find_left(data, pos[0])
            if k != -1:
                new_pos,dir = k
            else:
                new_pos = pos
        elif pos[1] + direction[dir][1] >= len(data[0]):
            k = find_right(data, pos[0])
            if k != -1:
                new_pos,dir = k
            else:
                new_pos = pos
        
        else:

            new_pos = [pos[0] + direction[dir][0], pos[1] + direction[dir][1]]

            if data[new_pos[0]][new_pos[1]] == "#":
                break
            elif data[new_pos[0]][new_pos[1]] == " ":
                if dir == "up":
                    k = find_up(data, pos[1])
                    if k != -1:
                        new_pos,dir = k
                    else:
                        new_pos = pos
                elif dir == "down":
                    k = find_down(data, pos[1], pos)
                    if k != -1:
                        new_pos,dir = k
                    else:
                        new_pos = pos
                elif dir == "left":
                    k = find_left(data, pos[0])
                    if k != -1:
                        new_pos,dir = k
                    else:
                        new_pos = pos
                elif dir == "right":
                    k = find_right(data, pos[0])
                    if k != -1:
                        new_pos,dir = k
                    else:
                        new_pos = pos
            elif data[new_pos[0]][new_pos[1]] == ".":
                pass
        
        pos = new_pos

    return pos, dir
    

a = get_col_size(filename)
data, moves, start_pos = read_file(filename, a)

dir = 'right'
pos = start_pos

pos,dir = move(data, pos, dir, moves[0][0])
for i in range(len(moves[1])):
    dir = change_dir(dir, moves[1][i])
    pos,dir = move(data, pos, dir, moves[0][i+1])

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