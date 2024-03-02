N = int(input())

n = 1000000

while N > 0:
    check = list(str(n))
    if check[4] == check[6]:
        N -= 1

    n += 1

n -= 1

n = list(str(n))

n.insert(1, n[0])
n.insert(5, n[4])

print("".join(n))