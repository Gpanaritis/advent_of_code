given_file = open('input.txt', 'r')

lines = given_file.readlines()

given_file.close()

def get_corrupt(line):
    temp = []
    for char in line:
        if char in ['(','<','[','{']:
            temp.append(char)
        elif char in [')','>',']','}']:
            if ord(char) == ord(temp[-1]) + 1 or ord(char) == ord(temp[-1]) + 2:
                temp.pop(-1)
            else:
                return char
    return temp

def calc_corrupt(line):
    temp = get_corrupt(line)
    if temp == ')':
        return 3
    elif temp == ']':
        return 57
    elif temp == '}':
        return 1197
    elif temp == '>':
        return 25137
    else:
        return 0

def part_1(lines):
    sum = 0
    for line in lines:
        sum += calc_corrupt(line)
    return sum

def calc_not_corrupt(line):
    sum = 0
    temp = get_corrupt(line)
    if temp not in [')','>',']','}']:
        for item in temp[::-1]:
            if item == '(':
                sum *= 5
                sum += 1
            elif item == '[':
                sum *= 5
                sum += 2
            elif item == '{':
                sum *= 5
                sum += 3
            elif item == '<':
                sum *= 5
                sum += 4
    return sum

def part_2(lines):
    arr = []
    for line in lines:
        temp = calc_not_corrupt(line)
        if temp > 0:
            arr.append(temp)
    arr.sort()
    return arr[len(arr)//2]
                
print(get_corrupt(lines[9]))

print(part_1(lines))
print(calc_not_corrupt(lines[9]))
print(part_2(lines))

