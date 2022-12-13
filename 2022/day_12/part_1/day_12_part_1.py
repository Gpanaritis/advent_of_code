class Node:
    def __init__(self, pos, height):
        self.pos = pos
        if height == 'S':
            self.height = ord('a') - 97
            self.is_start = True
            self.is_end = False
        elif height == 'E':
            self.height = ord('z') - 97
            self.is_start = False
            self.is_end = True
        else:
            self.height = ord(height) - 97
            self.is_start = False
            self.is_end = False
        self.parent = None
        self.deep = 0

def bfs(start, end, grid):

    queue = []
    queue.append(start)

    while len(queue) > 0:

        node = queue.pop(0)

        if node.is_end:
            return node
        
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                if i != 0 and j != 0:
                    continue
                if node.pos[0] + i < 0 or node.pos[0] + i >= len(grid):
                    continue
                if node.pos[1] + j < 0 or node.pos[1] + j >= len(grid[0]):
                    continue
                if grid[node.pos[0] + i][node.pos[1] + j].height > node.height + 1:
                    continue
                if grid[node.pos[0] + i][node.pos[1] + j] in queue:
                    continue

                grid[node.pos[0] + i][node.pos[1] + j].parent = node
                grid[node.pos[0] + i][node.pos[1] + j].deep = node.deep + 1
                queue.append(grid[node.pos[0] + i][node.pos[1] + j])
    return None

a = []

f = open('test.txt', 'r')

for i,line in enumerate(f):
    line = line.strip()
    a.append([])
    for j,c in enumerate(line):
        if c == 'S':
            start = (i,j)
        elif c == 'E':
            end = (i,j)
        a[i].append(Node((i,j), c))

f.close()

start_node = a[start[0]][start[1]]
end_node = a[end[0]][end[1]]

visited = set()

node = bfs(start_node, end_node, a)

print(node.deep)





        
        
