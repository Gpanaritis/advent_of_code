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

def calc_monkey(monkey):
    print(monkey)
    if type(monkeys[monkey]) == int:
        return monkeys[monkey]
    else:
        # do operation with monkey[1]
        return int(eval(f'calc_monkey(monkeys[monkey][0]) {monkeys[monkey][1]} calc_monkey(monkeys[monkey][2])'))

monkeys = read_file('data.txt')
res = calc_monkey('root')
print(res)
