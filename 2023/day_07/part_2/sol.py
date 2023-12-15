from collections import Counter

hands = []

with open('data.txt') as f:
    lines = f.readlines()

for line in lines:
    hands.append(line.strip().split(' '))

help_map = {'A': 'Z', 'K': 'Y', 'Q': 'X', 'T': 'V', '9': 'U', '8': 'T', '7': 'S', '6': 'R', '5': 'Q', '4': 'P', '3': 'O', '2': 'N', 'J': 'M'}

def get_points(hand):
    cards = hand[0]
    cards3 = ''.join([help_map[card] for card in cards])
    cards_counter = Counter(cards)

    # Five pair
    if len(cards_counter) == 1:
        return 'Z' + cards3
    # Four of a kind
    elif len(cards_counter) == 2 and cards_counter.most_common(1)[0][1] == 4:
        # Five of a kind with Joker
        if 'J' in hand[0]:
            return 'Z' + cards3
        else:
            return 'Y' + cards3
    # Full house
    elif cards_counter.most_common(1)[0][1] == 3 and cards_counter.most_common(2)[1][1] == 2:
        # Five of a kind with Joker
        if 'J' in hand[0]:
            return 'Z' + cards3
        else:
            return 'X' + cards3
    # Three of a kind
    elif len(cards_counter) == 3 and cards_counter.most_common(1)[0][1] == 3:
        # Four of a kind with Joker
        if 'J' in hand[0]:
            return 'Y' + cards3
        else:
            return 'W' + cards3
    # Two double pairs
    elif len(cards_counter) == 3 and cards_counter.most_common(1)[0][1] == 2:
        # Four of a kind with 2 Jokers
        if 'J' in hand[0] and cards_counter['J'] == 2:
            return 'Y' + cards3
        # Fullhouse with one Joker
        elif 'J' in hand[0]:
            return 'X' + cards3
        else:
            return 'V' + cards3
    # Two of a kind
    elif len(cards_counter) == 4 and cards_counter.most_common(1)[0][1] == 2:
        if 'J' in hand[0]:
            return 'W' + cards3
        else:
            return 'U' + cards3
    # High card
    else:
        if 'J' in hand[0]:
            return 'U' + cards3
        else:
            return 'T' + cards3

sorted_hands = sorted(hands, key=lambda x: get_points(x))

s = 0
for i in range(len(sorted_hands)):
    s += int(sorted_hands[i][1]) * (i+1)
print(s)