from collections import defaultdict


N = int(input())
S = input()

check = defaultdict(int)

for s in S:
    check[s] += 1
    
teck = ["T", "E", "C", "H"]


ans = 10 ** 20

for i in teck:
    ans = min(ans, check[i])
    
print(ans)