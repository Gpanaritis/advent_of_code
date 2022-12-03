def count_different(str1,str2):
    sum = 0
    for c in ['a','b','c','d','e','f','g']:
        if c in str1 and c not in str2 or c in str2 and c not in str1:
            sum += 1
    return sum

def find_strings(part_2):
    nums = ["" for i in range(10)]

   # for line in part_2:
    for str in part_2:
        if len(str) == 2:
            nums[1] = str
        if len(str) == 3:
            nums[7] = str
        if len(str) == 4:
            nums[4] = str
        if len(str) == 7:
            nums[8] = str
    for str in part_2:
        if len(str) == 6 and count_different(nums[4],str) == 2:
            nums[9] = str
    for str in part_2:
        if len(str) == 6 and count_different(nums[7],str) == 3 and str != nums[9]:
            nums[0] = str
    for str in part_2:
        if len(str) == 6 and str not in [nums[0],nums[9]]:
            nums[6] = str
    for str in part_2:
        if len(str) == 5 and count_different(nums[7],str) == 2:
            nums[3] = str
    for str in part_2:
        if len(str) == 5 and count_different(nums[6],str) == 1:
            nums[5] = str
    for str in part_2:
        if len(str) == 5 and str not in [nums[3],nums[5]]:
            nums[2] = str

    return nums

given_file = open('input.txt', 'r')

lines = given_file.readlines()

given_file.close()

all = []

for line in lines:
    all.append(line.split(' | ')[1].replace('\n',''))

segment_display = []

for line in all:
    segment_display.extend(line.split(' '))

sum = 0

for num in segment_display:
    if len(num) in [2,3,4,7]:
        sum += 1

all = []
for line in lines:
    all.append([line.split(' | ')[0],line.split(' | ')[1].replace('\n','')])

part_2 = []
for line in all:
    part_2.append([line[0].split(' '),line[1].split(' ')])


sum = 0
for line in part_2:
    nums = find_strings(line[0])
    nums = [sorted(nums[i]) for i in range(10)]
    num = ""
    for string in line[1]:
        num += str(nums.index(sorted(string)))
    sum += int(num)
print(sum)

