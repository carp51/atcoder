from collections import defaultdict
import math


def combinations_count(n, k):
    return math.factorial(n) // (math.factorial(n - k) * math.factorial(k))

S = list(map(int, input()))

bit = [0 for i in range(10)]

bit_l = ['0000000000']
bit_check = defaultdict(int)

bit_check['0000000000'] = 1

for i in range(len(S)):
    if bit[S[i]] == 0:
        bit[S[i]] = 1
    else:
        bit[S[i]] = 0
        
    bit = list(map(str, bit))
    
    bit = "".join(bit)
    bit_check[bit] += 1
    bit_l.append(bit)
    
    bit = list(map(int, bit))
    
ans = 0

for i in bit_check.values():
    if i < 2:
        continue
    ans += combinations_count(i, 2)
    
print(ans)