class Node:
    def __init__(self,name,type,subs,size,parent):
        self.name = name
        self.type = type
        self.subs = subs
        self.size = size
        self.parent = parent

def get_size(node):
    if node.type == "file":
        return node.size
    else:
        for sub in node.subs:
            node.size += get_size(sub)
        return node.size

def get_sum(node):
    global sum
    if node.type == "dir" and node.size < 100000:
        sum += node.size
    for sub in node.subs:
        get_sum(sub)

def choose_to_delete(node,need):
    global min
    if node.type == "dir" and node.size >= need and node.size < min:
        min = node.size
    for sub in node.subs:
        choose_to_delete(sub,need)




f = open("test.txt","r")

root = Node("/","dir",[],0,None)

cur = root

for line in f:
    line = line.strip()
    line = line.split(" ")

    if line[0] == "$" and line[1] == "cd":
        if(line[2] == ".."):
            cur = cur.parent
        else:
            for sub in cur.subs:
                if sub.name == line[2]:
                    cur = sub
        continue

    elif line[0] == "$" and line[1] == "ls":
        continue

    elif line[0] == "dir":
        cur.subs.append(Node(line[1],"dir",[],0,cur))
        continue

    else:
        cur.subs.append(Node(line[1],"file",[],int(line[0]),cur))
        continue

get_size(root)

# for i in root.subs:
#     print(i.name, i.size)
sum = 0

disk = 70000000
update = 30000000

space = disk - root.size

need = update - space

if need < 0:
    print("No need to delete")
else:
    min = root.size
    choose_to_delete(root,need)
    print(min)