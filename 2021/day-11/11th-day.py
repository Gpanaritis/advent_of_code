given_file = open('example.txt', 'r')

lines = given_file.readlines()

given_file.close()

def flash(arr,i,j):
    sum = 0
    if arr[i][j] == 0:
        return 0

    if arr[i][j] > 9:
        arr[i][j] = 0
        sum += 1
        for n in neighbors(arr,i,j):
            sum += flash(arr,n[0],n[1])
    return sum

def neighbors(matrix, rowNumber, colNumber):
    result = []
    for rowAdd in range(-1, 2):
        newRow = rowNumber + rowAdd
        if newRow >= 0 and newRow <= len(matrix)-1:
            for colAdd in range(-1, 2):
                newCol = colNumber + colAdd
                if newCol >= 0 and newCol <= len(matrix)-1:
                    if newCol == colNumber and newRow == rowNumber:
                        continue
                    result.append([newCol,newRow])
    return result

lines = [list(map(int, x[:-1])) for x in lines]
lines[len(lines)-1].append(6)

sum = 0

for k in range(1):
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            lines[i][j] += 1

    for i in range(len(lines)):
        for j in range(len(lines[0])):
            sum += flash(lines,i,j)

print(sum)
print(lines)