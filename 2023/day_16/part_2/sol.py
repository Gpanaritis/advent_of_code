import sys


def read_input():
    with open(sys.argv[1]) as f:
        f = f.readlines()
        return [list(line.strip()) for line in f]

def move_one_step(beams, grid):
    new_beams = {"location": [], "direction": []}
    for _ in range(len(beams["location"])):
        i, j = beams["location"].pop()
        di, dj = beams["direction"].pop()
        if i + di < 0 or i + di >= len(grid) or j + dj < 0 or j + dj >= len(grid[0]):
            continue
        new_i, new_j = i + di, j + dj
        if grid[new_i][new_j] == "/":
            new_di, new_dj = -dj, -di
            new_beams["location"].append((new_i, new_j))
            new_beams["direction"].append((new_di, new_dj))
        elif grid[new_i][new_j] == "\\":
            new_di, new_dj = dj, di
            new_beams["location"].append((new_i, new_j))
            new_beams["direction"].append((new_di, new_dj))
        elif grid[new_i][new_j] == "|" and di == 0:
            new_beams["location"].append((new_i, new_j))
            new_beams["direction"].append((-1, 0))
            new_beams["location"].append((new_i, new_j))
            new_beams["direction"].append((1, 0))
        elif grid[new_i][new_j] == "-" and dj == 0:
            new_beams["location"].append((new_i, new_j))
            new_beams["direction"].append((0, -1))
            new_beams["location"].append((new_i, new_j))
            new_beams["direction"].append((0, 1))
        else:
            new_beams["location"].append((new_i, new_j))
            new_beams["direction"].append((di, dj))

    return new_beams

def traverse(grid, start, direction):

    i,j = start
    di, dj = direction
    
    if grid[i][j] == "/":
        new_di, new_dj = -dj, -di
        beams = {"location": [(i, j)], "direction": [(new_di, new_dj)]}
    elif grid[i][j] == "\\":
        new_di, new_dj = dj, di
        beams = {"location": [(i, j)], "direction": [(new_di, new_dj)]}
    elif grid[i][j] == "|" and di == 0:
        beams = {"location": [(i, j),(i,j)], "direction": [(-1, 0), (1, 0)]}
    elif grid[i][j] == "-" and dj == 0:
        beams = {"location": [(i, j),(i,j)], "direction": [(0, -1), (0, 1)]}
    else:
        beams = {"location": [(i, j)], "direction": [(di, dj)]}


    energy_grid = set()
    while beams["location"]:
        i = 0
        while i < len(beams["location"]):
            if (beams["location"][i], beams["direction"][i]) in energy_grid:
                beams["location"].pop(i)
                beams["direction"].pop(i)
            else:
                energy_grid.add((beams["location"][i], beams["direction"][i]))
                i += 1
        beams = move_one_step(beams, grid)
    final_energy_grid = set()
    for location, direction in energy_grid:
        final_energy_grid.add(location)
    return final_energy_grid

def try_all(grid):
    max_energy = 0
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            for direction in directions:
                new_i, new_j = i + direction[0], j + direction[1]
                if 0 <= new_i < len(grid) and 0 <= new_j < len(grid[0]):
                    max_energy = max(max_energy, len(traverse(grid, (i, j), direction)))

    return max_energy




def main():
    grid = read_input()
    energized = try_all(grid)
    print(energized)


if __name__ == '__main__':
    main()