import heapq
from collections import defaultdict

N, Q = map(int, input().split())

l = [i for i in range(1, N + 1)]

l.sort(reverse=True)

machi_l = []
heapq.heapify(machi_l)

check = defaultdict(int)

for i in range(Q):
    e = list(map(int, input().split()))
    if e[0] == 1:
        machi_l.append(l[-1])
        l.pop()
    elif e[0] == 2:
        x = e[1]
        check[x] = 1
    else:
        while True:
            tmp = heapq.heappop(machi_l)
            if check[tmp] == 0:
                print(tmp)
                heapq.heappush(machi_l, tmp)
                break
        