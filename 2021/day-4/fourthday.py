class set:
    def __init__(self,number):
        self.number = number
        self.isTrue = False

class bingo:
    def __init__(self,arr):
        self.completed = False
        rows, cols = (5, 5)
        self.arr = []
        for i in range(rows):
            col = []
            for j in range(cols):
                col.append(set(int(arr[i][j])))
            self.arr.append(col)
    
    def print(self):
        for i in range (0,5):
            for j in range (0,5):
                print(self.arr[i][j].number,self.arr[i][j].isTrue,end=' ')
            print()
    
    def new_num(self,num):
        for i in range (0,5):
            for j in range (0,5):
                if num == self.arr[i][j].number:
                    self.arr[i][j].isTrue = True
                    self.check_bingo(i,j)
    
    def check_bingo(self,row,col):
        temp_row = True
        temp_col = True
        for i in range(0,5):
            temp_row *= self.arr[i][col].isTrue
            temp_col *= self.arr[row][i].isTrue
        
        if temp_row or temp_col:
            self.completed = True
    
    def sum_unmarked(self):
        sum = 0
        for i in range (0,5):
            for j in range (0,5):
                if not self.arr[i][j].isTrue:
                    sum += self.arr[i][j].number
        return sum
        

def remove_s(col):
    N = ''
    for sub in col:
        sub[:] = [ele for ele in sub if ele != N]

def find_completed(bingos):
    for i in range (0,len(bingos)):
        if bingos[i].completed:
            return i;
    return -1

def find_uncompleted(bingos):
    sum = 0
    for bingo in bingos:
        if not bingo.completed:
            sum += 1
    return sum

def find_last(bingos):
    for i in range (0,len(bingos)):
        if not bingos[i].completed:
            return i;
#read input file
given_file = open('input.txt', 'r')

lines = given_file.readline()

input = lines.split(',')

given_file.close()

#read bingo file
bingos = []

col = []
with open('bingo.txt') as openfileobject:
    for line in openfileobject:
        col.append(line.split(' '))
        if line == '\n':
            remove_s(col)
            bingos.append(bingo(col))
            col = []

remove_s(col)
bingos.append(bingo(col))
bingos_2 = bingos.copy()

for num in input:
    for bingo in bingos:
        bingo.new_num(int(num))
    is_completed = find_completed(bingos)
    if is_completed != -1:
        break

'''
print(is_completed)
print(bingos[is_completed].sum_unmarked())
print(bingos[is_completed].sum_unmarked()*int(num))
'''
for num in input:
    for bingo in bingos_2:
        bingo.new_num(int(num))
    uncompleted = find_uncompleted(bingos_2)
    if uncompleted == 1:
        last_bingo = bingos[find_last(bingos)]
    if uncompleted == 0:
        break

print(last_bingo.sum_unmarked()*int(num))
