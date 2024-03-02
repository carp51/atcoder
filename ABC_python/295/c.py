N = int(input())
A = list(map(int, input().split()))

from collections import defaultdict

check = defaultdict(int)

for i in A:
    check[i] += 1
    
ans = 0

for i in check.values():
    ans += i //2
    
print(ans)