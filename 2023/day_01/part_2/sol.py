import regex as re

with open('data.txt') as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]

s = 0

map_ints = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'zero': 0, '0': 0, '1': 1, '2': 2, '3': 3, '4': 4,'5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

pattern = r"(?:\d|zero|one|two|three|four|five|six|seven|eight|nine)"


for line in lines:
    # find all matches
    matches = re.findall(pattern, line)
    # convert all matches to ints
    matches = re.findall(pattern, line, overlapped=True)
    # sum first and last
    s += int(str(map_ints[matches[0]]) + str(map_ints[matches[-1]]))

print(s)