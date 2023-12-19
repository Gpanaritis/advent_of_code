import sys
import heapq

def read_input():
    with open(sys.argv[1], 'r') as f:
       lines = f.readlines()
    return [list(map(int, list(line.strip()))) for line in lines]

def dijkstra(grid, start, end):
    queue = [(start, (0, 0), 0, 0, None)]
    cost_grid = [[float('inf') for _ in range(len(grid[0]))] for _ in range(len(grid))]
    visited = {}
    while queue:
        queue.sort(key=lambda x: x[3], reverse=True)
        pos, dir, num_steps, cost, prev = queue.pop()
        cost_grid[pos[0]][pos[1]] = min(cost_grid[pos[0]][pos[1]], cost)

        if pos == end:
            break
        if (pos, dir, num_steps) in visited.keys() and cost >= visited[(pos, dir, num_steps)]: 
            continue
        visited[(pos, dir, num_steps)] = cost
        for d in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_pos = (pos[0] + d[0], pos[1] + d[1])
            if new_pos == prev:
                continue
            if new_pos[0] < 0 or new_pos[0] >= len(grid) or new_pos[1] < 0 or new_pos[1] >= len(grid[0]):
                continue
            if d == dir and num_steps == 3:
                continue
            if d == dir:
                queue.append((new_pos, d, num_steps + 1, cost + grid[new_pos[0]][new_pos[1]], pos))
            else:
                queue.append((new_pos, d, 1, cost + grid[new_pos[0]][new_pos[1]], pos))
    return cost_grid[end[0]][end[1]], cost_grid

def main():
    
    grid = read_input()
    start = (0, 0)
    end = (len(grid) - 1, len(grid[0]) - 1)
    cost, cost_grid = dijkstra(grid, start, end)
    
    print(cost)


if __name__ == '__main__':
    main()