with open("data.txt", "r") as f:
    lines = list(map(lambda x: x.strip(), f.readlines()))

games = []
red_cubes = 12
green_cubes = 13
blue_cubes = 14
s = 0

for line in lines:
    l = line.split(': ')[1]
    l = l.split('; ')
    l = list(map(lambda x: list(map(lambda y: y.split(' '), x.split(', '))), l))
    games.append(l)

for i,game in enumerate(games):

    max_red = 0
    max_blue = 0
    max_green = 0

    for turn in game:
        for pick in turn:
            if pick[1] == 'red':
                max_red = max(max_red, int(pick[0]))
            if pick[1] == 'blue':
                max_blue = max(max_blue, int(pick[0]))
            if pick[1] == 'green':
                max_green = max(max_green, int(pick[0]))
    
    if red_cubes >= max_red and blue_cubes >= max_blue and green_cubes >= max_green:
        s += i + 1

print(s)

    