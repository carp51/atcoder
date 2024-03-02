n = int(input('n:'))
newlist = []
emlist = []
for x in range(1, n + 1):
    emlist = []
    for y in range(1, n + 1):
        if x % y == 0:
            emlist.append(y)
    newlist.append([a for a in emlist])
print(newlist)
