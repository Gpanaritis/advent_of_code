histories = []

with open('data.txt') as f:
    lines = f.readlines()
    for line in lines:
        histories.append(list(map(int,line.strip().split())))

def get_prediction(history):
    if len(history) == 0:
        return 0
    if history.count(0) == len(history):
        return 0
    return history[-1] + get_prediction([history[i + 1] - history[i] for i in range(len(history)-1)]) 

s = 0

for history in histories:
    s += get_prediction(history)

print(s)