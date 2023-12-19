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

def traverse(grid):
    if grid[0][0] == "|" or grid[0][0] == "\\":
        beams = {"location": [(0, 0)], "direction": [(1, 0)]}
    elif grid[0][0] == "/":
        beams = {"location": [(0, 0)], "direction": [(-1, 0)]}
    else:
        beams = {"location": [(0, 0)], "direction": [(0, 1)]}


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




def main():
    grid = read_input()
    energy_grid = traverse(grid)
    print(len(energy_grid))


if __name__ == '__main__':
    main()