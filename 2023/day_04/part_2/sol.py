with open('data.txt') as f:
    lines = f.readlines()

cards = []
s = 0

for line in lines:
    l = line.strip()
    l = l.split(': ')[1]
    l = l.split(' | ')
    l = [x.split(' ') for x in l]
    l = [[int(y) for y in x if y.isnumeric()] for x in l]
    cards.append(l)

cards_copies = [1] * len(cards)

for i,card in enumerate(cards):
    same = len(set(card[0]) & set(card[1]))
    for j in range(1,same+1):
        cards_copies[i+j] += cards_copies[i]

s = sum(cards_copies)
print(s)
