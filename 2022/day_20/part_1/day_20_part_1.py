f = open('data.txt', 'r')

a = {}
b = []
c = set()
counter = 0

for line in f:
    line = line.strip()
    a.update({counter: int(line)})
    b.append(counter)
    counter += 1

for key in a:
    i = b.index(key)
    c = a[b.pop(i)]

    if (i + c) > 0 and (i + c) < len(a):
        b.insert(i+c,key)
    elif (i + c) == 0:
        b.append(key)
    elif (i + c) == len(a) - 1:
        b.insert(0,key)
    elif (i + c) > len(a) - 1:
        b.insert((i+c) % len(b),key)
    elif (i + c) < 0:
        b.insert((i+c) % len(b),key)
    
    # for i in b:
    #     print(a[i], end = ' ')
    # print()

#find key of value 0 from dictionary
for key in a:
    if a[key] == 0:
        f = key
        break


i = b.index(f)
print(i)
print(sum([a[b[i+1000]], a[b[i+2000]], a[b[i+3000]]]))

# for i in b:
#     print(a[i], end = ' ')


# try:
#     while True:
#         if len(seen) == len(a):
#             break
#         for i,b in enumerate(a):
#             if i == len(a) - 1:
#                 raise StopIteration
#             if b in seen:
#                 continue
#             if b not in seen:
#                 seen.add(b)
#                 c = a.pop(i)
#                 if (i + c) % len(a) > 0:
#                     a.insert((i+c) % len(a),c)
#                 elif (i + c) % len(a) <= 0 :
#                     print('here')
#                     a.insert((i+c-1) % len(a),c)
#                 print(i, len(a) - len(seen), (i+c) % len(a))
#                 print(i, len(a) - len(seen), (i+b) % len(a))
#                 break
# except StopIteration:
#     pass

# i = a.index(0)
# # print(sum([a[i+1000], a[i+2000], a[i+3000]]))
# print(i)