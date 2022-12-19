import re
import math
import sys

class Node:
    def __init__(self,ore, ore_robots, clay, clay_robots, obsidian, obsidian_robots, geode, geode_robots, depth):
        self.ore = ore
        self.ore_robots = ore_robots
        self.clay = clay
        self.clay_robots = clay_robots
        self.obsidian = obsidian
        self.obsidian_robots = obsidian_robots
        self.geode = geode
        self.geode_robots = geode_robots
        self.children = []
        self.min_geode = 24
        self.depth = depth

def step():
    global b
    global cur_node
    global n
    global remaining
    global max_geode_robots
    global max_obsidian_robots
    global max_clay_robots

    choices = []

    # print(b[0], n[cur_node].ore)

    if b[0] <= n[cur_node].ore:
        choices.append('make_ore')
    if b[1] <= n[cur_node].ore:
        choices.append('make_clay')
    if b[2][0] <= n[cur_node].ore and b[2][1] <= n[cur_node].clay:
        choices.append('make_obsidian')
    if b[3][0] <= n[cur_node].ore and b[3][1] <= n[cur_node].obsidian:
        choices.append('make_geode')


    if 'make_geode' in choices:
        choices = ['make_geode']
    elif n[cur_node].geode_robots < max_geode_robots:
        return
    elif n[cur_node].obsidian_robots < max_obsidian_robots - 3:
        return
    elif n[cur_node].clay_robots < max_clay_robots - 5:
        return

    if 'make_clay' in choices and n[cur_node].clay_robots >= b[2][1]:
        choices.remove('make_clay')
    if 'make_obsidian' in choices and n[cur_node].obsidian_robots >= b[3][1]:
        choices.remove('make_obsidian')
    if 'make_ore' in choices and n[cur_node].ore_robots >= max(b[1],b[2][0],b[3][0]):
        choices.remove('make_ore')
        

    if not('make_clay' in choices and 'make_obsidian' in choices and 'make_ore' in choices):
        ore = n[cur_node].ore + n[cur_node].ore_robots
        ore_robots = n[cur_node].ore_robots
        clay = n[cur_node].clay + n[cur_node].clay_robots
        clay_robots = n[cur_node].clay_robots
        obsidian = n[cur_node].obsidian + n[cur_node].obsidian_robots
        obsidian_robots = n[cur_node].obsidian_robots
        geode = n[cur_node].geode + n[cur_node].geode_robots
        geode_robots = n[cur_node].geode_robots
        depth = n[cur_node].depth + 1
        n.append(Node(ore, ore_robots, clay, clay_robots, obsidian, obsidian_robots, geode, geode_robots,depth))
        n[cur_node].children.append(len(n) - 1)

    
    for c in choices:
        if c == 'make_ore':
            ore = n[cur_node].ore - b[0] + n[cur_node].ore_robots
            ore_robots = n[cur_node].ore_robots + 1
            clay = n[cur_node].clay + n[cur_node].clay_robots
            clay_robots = n[cur_node].clay_robots
            obsidian = n[cur_node].obsidian + n[cur_node].obsidian_robots
            obsidian_robots = n[cur_node].obsidian_robots
            geode = n[cur_node].geode + n[cur_node].geode_robots
            geode_robots = n[cur_node].geode_robots
        elif c == 'make_clay':
            ore = n[cur_node].ore - b[1] + n[cur_node].ore_robots
            ore_robots = n[cur_node].ore_robots
            clay = n[cur_node].clay + n[cur_node].clay_robots
            clay_robots = n[cur_node].clay_robots + 1
            obsidian = n[cur_node].obsidian + n[cur_node].obsidian_robots
            obsidian_robots = n[cur_node].obsidian_robots
            geode = n[cur_node].geode + n[cur_node].geode_robots
            geode_robots = n[cur_node].geode_robots
        elif c == 'make_obsidian':
            ore = n[cur_node].ore - b[2][0] + n[cur_node].ore_robots
            ore_robots = n[cur_node].ore_robots
            clay = n[cur_node].clay - b[2][1] + n[cur_node].clay_robots
            clay_robots = n[cur_node].clay_robots
            obsidian = n[cur_node].obsidian + n[cur_node].obsidian_robots
            obsidian_robots = n[cur_node].obsidian_robots + 1
            geode = n[cur_node].geode + n[cur_node].geode_robots
            geode_robots = n[cur_node].geode_robots
        elif c == 'make_geode':
            ore = n[cur_node].ore - b[3][0] + n[cur_node].ore_robots
            ore_robots = n[cur_node].ore_robots
            clay = n[cur_node].clay + n[cur_node].clay_robots
            clay_robots = n[cur_node].clay_robots
            obsidian = n[cur_node].obsidian - b[3][1] + n[cur_node].obsidian_robots
            obsidian_robots = n[cur_node].obsidian_robots
            geode = n[cur_node].geode + n[cur_node].geode_robots
            geode_robots = n[cur_node].geode_robots + 1
        depth = n[cur_node].depth + 1
        n.append(Node(ore, ore_robots, clay, clay_robots, obsidian, obsidian_robots, geode, geode_robots, depth))
        n[cur_node].children.append(len(n)-1)

    # print(cur_node, choices, n[cur_node].children)



f = open('data.txt', 'r')

blueprints = []

for line in f:
    line = line.strip()
    a = [int(s) for s in re.findall(r'\b\d+\b', line)]
    b = [a[1],a[2],[a[3],a[4]],[a[5],a[6]],a[0]]
    blueprints.append(b)

f.close()

n = []

root = Node(0,1,0,0,0,0,0,0,0)

n.append(root)
cur_node = 0
remaining = 24
b = blueprints[int(sys.argv[1])]
max_geode_robots = 0
max_obsidian_robots = 0
max_clay_robots = 0

for i in range(32):
    for k in range(len(n)):
        if n[k].depth == i:
            cur_node = k
            step()
    remaining -= 1

    for l in n:
        if l.geode_robots > max_geode_robots:
            max_geode_robots = l.geode_robots
        if l.obsidian_robots > max_obsidian_robots:
            max_obsidian_robots = l.obsidian_robots
        if l.clay_robots > max_clay_robots:
            max_clay_robots = l.clay_robots
    print(i,max_geode_robots,max_obsidian_robots,max_clay_robots)

    if i == 30:
        max = n[0]
        for i in n:
            if i.geode + i.geode_robots > max.geode + max.geode_robots:
                max = i
        print(max.geode + max.geode_robots, sys.argv[1])
        break

# print(n[24].children,n[26].children,n[27].children)
# max = n[0]
# for i in n:
#     if i.geode > max.geode:
#         max = i
# print(max.geode, sys.argv[1])