with open('data.txt') as f:
    lines = f.readlines()

cards = []
s = 0

for line in lines:
    l = line.strip()
    l = l.split(': ')[1]
    # if 
    l = l.split(' | ')
    l = [x.split(' ') for x in l]
    l = [[int(y) for y in x if y.isnumeric()] for x in l]
    cards.append(l)

for card in cards:
    # How many same numbers in card[0] and card[1]
    points = len(set(card[0]) & set(card[1]))
    points = 0 if points == 0 else 2**(points-1)
    s += points
print(s)

