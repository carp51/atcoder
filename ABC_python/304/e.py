from collections import defaultdict
from bisect import bisect_right


W, H = map(int, input().split())
N = int(input())
pq = []

for i in range(N):
    p, q = map(int, input().split())
    pq.append([p, q])
    
A = int(input())
a = list(map(int, input().split()))
B = int(input())
b = list(map(int, input().split()))

a.insert(0, 0)
b.insert(0, 0)
a.append(10 ** 20)
b.append(10 ** 20)

check = defaultdict(int)

for i in range(N):
    p, q = pq[i][0], pq[i][1]
    check[((bisect_right(a, p), bisect_right(a, p) - 1), (bisect_right(b, q), bisect_right(b, q) - 1))] += 1

check_num = 0
min_num = 10 ** 20
max_num = -10

for i, j in check.items():
    check_num += 1
    
    min_num = min(min_num, j)
    max_num = max(max_num, j)
    
if (A + 1) * (B + 1) != check_num:
    min_num = 0
    
print(min_num, max_num)
