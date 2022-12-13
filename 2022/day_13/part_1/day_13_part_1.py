def compare_lists(list1, list2):
    try:
        if type(list1) == int and type(list2) == int:
            return list2 - list1
        elif type(list1) == list and type(list2) == int:
            return compare_lists(list1,[list2])
        elif type(list1) == int and type(list2) == list:
            return compare_lists([list1], list2)

        for i in range(max(len(list1), len(list2))):
            a = compare_lists(list1[i], list2[i])
            if a > 0:
                return 1
            elif a < 0:
                return -1
        return 0
    except IndexError:
        if len(list1) < len(list2):
            return 1
        elif len(list1) > len(list2):
            return -1
        return 0
        


f = open('test.txt', 'r')

indices = []

a = []
b = []
count = 0

for line in f:

    if count  % 3 == 0:
        line = line.strip()

        c = 'a = ' + line
        exec(c)
    
    elif count  % 3 == 1:
        line = line.strip()

        c = 'b = ' + line
        exec(c)
    elif count % 3 == 2:
        c = compare_lists(a, b)
        if c == 1:
            indices.append(count // 3 + 1)

    count += 1

c = compare_lists(a, b)
if c == 1:
    indices.append(count // 3 + 1)

print(sum(indices))

f.close()

