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
def insertion_sort(list1,item):
    for i in range(len(list1)):
        if compare_lists(item, list1[i]) == 1:
            list1.insert(i, item)
            return list1
    list1.append(item)
    return list1
        


f = open('data.txt', 'r')

a = []
b = []
all = []
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
        all = insertion_sort(all, a)
        all = insertion_sort(all, b)

    count += 1

all = insertion_sort(all, a)
all = insertion_sort(all, b)

all = insertion_sort(all, [[2]])
all = insertion_sort(all, [[6]])

decoder_key = 1

for i in range(len(all)):
    if all[i] == [[2]]:
        decoder_key *= i + 1
    elif all[i] == [[6]]:
        decoder_key *= i + 1

print(decoder_key)

f.close()

