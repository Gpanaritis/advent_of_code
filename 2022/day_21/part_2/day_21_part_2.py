def read_file(file_name):
    f = open(file_name, 'r')

    a = {}

    for line in f:
        line = line.strip()
        line = line.split(':')
        line[1] = line[1].strip()
        line[1] = line[1].split(' ')
        if len(line[1]) == 1:
            line[1] = int(line[1][0])
        a.update({line[0]: line[1]})

    f.close()
    return a

def calc_monkey(key):
    global monkeys

    if type(monkeys[key]) == int:
        return monkeys[key]
    else:
        temp_res = int(eval(f'calc_monkey(monkeys[key][0]) {monkeys[key][1]} calc_monkey(monkeys[key][2])'))
        monkeys[key].append(temp_res)
        return temp_res

def humn_is_child(key):
    if key == 'humn':
        return True
    else:
        if type(monkeys[key]) == int:
            return False
        else:
            return humn_is_child(monkeys[key][0]) or humn_is_child(monkeys[key][2])

def find_humn(key,value):
    global monkeys
    children = monkeys[key]

    if key == 'humn':
        monkeys[key] = value
        return int(value)
    
    monkeys[key].append(value)

    if humn_is_child(children[0]):
        i = 0
    elif humn_is_child(children[2]):
        i = 2
    
    if i == 0:
        value_2 = monkeys[children[2]]
        if type(value_2) != int:
            value_2 = value_2[3]
        if children[1] == '+':
            value = value - value_2
        elif children[1] == '-':
            value = value + value_2
        elif children[1] == '*':
            value = value / value_2
        elif children[1] == '/':
            value = value * value_2
    elif i == 2:
        value_2 = monkeys[children[0]]
        if type(value_2) != int:
            value_2 = value_2[3]
        if children[1] == '+':
            value = value - value_2
        elif children[1] == '-':
            value = value_2 - value
        elif children[1] == '*':
            value = value / value_2
        elif children[1] == '/':
            value = value_2 / value
    
    temp_res = find_humn(children[i],value)
    return temp_res


monkeys = read_file('data.txt')

want = calc_monkey('root')


if humn_is_child(monkeys['root'][0]):
    h = find_humn(monkeys['root'][0],monkeys[monkeys['root'][2]][3])

elif humn_is_child(monkeys['root'][2]):
    h = find_humn(monkeys['root'][2],monkeys[monkeys['root'][0]][3])

print(h)

