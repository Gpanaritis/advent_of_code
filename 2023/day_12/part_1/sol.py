import itertools

springs = []
nums = []

with open('data.txt') as f:
    lines = f.readlines()

for line in lines:
    line = line.strip().split(' ')
    springs.append(list(line[0]))
    nums.append(list(map(int, line[1].split(','))))

def check_spring(spring, nums):
    spring = ''.join(spring).split('.')
    n = [len(x) for x in spring if len(x) > 0]

    # return true if n is equal to nums
    return n == nums

count_corect_springs = []

for spring, num in zip(springs, nums):
    count_corect_springs.append(0)
    # get index of all # in spring
    idx = [i for i, x in enumerate(spring) if x == '?']

    perms = itertools.product('.#', repeat=len(idx))
    
    for perm in perms:

        for i, p in zip(idx, perm):
            spring[i] = p

        if check_spring(spring, num):
            count_corect_springs[-1] += 1

print(sum(count_corect_springs))