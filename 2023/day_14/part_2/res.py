x = 1000000000
#  Here you put where 125 the starting point of the repeating pattern
y = x - 125 + 1
# 26 is the length of the repeating pattern
y = y % 26

# The result is located in the line y + starting point of the repeating pattern
# Go look it up in the result file of sol.py
print(y + 124)