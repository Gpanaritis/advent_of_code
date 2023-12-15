with open("data.txt", "r") as f:
    lines = list(map(lambda x: x.strip(), f.readlines()))

games = []
s = 0

for line in lines:
    l = line.split(': ')[1]
    l = l.split('; ')
    l = list(map(lambda x: list(map(lambda y: y.split(' '), x.split(', '))), l))
    games.append(l)

for i,game in enumerate(games):

    max_min_red = 0
    max_min_blue = 0
    max_min_green = 0

    for turn in game:
        min_red = 999999999999
        min_blue = 999999999999
        min_green = 999999999999

        for pick in turn:
            if pick[1] == 'red':
                min_red = min(min_red, int(pick[0]))
            if pick[1] == 'blue':
                min_blue = min(min_blue, int(pick[0]))
            if pick[1] == 'green':
                min_green = min(min_green, int(pick[0]))
        
        if min_red == 999999999999:
            min_red = 1
        if min_blue == 999999999999:
            min_blue = 1
        if min_green == 999999999999:
            min_green = 1
        
        max_min_red = max(max_min_red, min_red)
        max_min_blue = max(max_min_blue, min_blue)
        max_min_green = max(max_min_green, min_green)
    
    s += max_min_red * max_min_blue * max_min_green

print(s)



    