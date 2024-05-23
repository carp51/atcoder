from collections import defaultdict
import math

def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a


N = int(input())
A = list(map(int, input().split()))

check = defaultdict(int)
ans = 0

min_num = A[0]

for i in range(1, N):
    min_num = math.gcd(min_num, A[i])

for i in range(N):
    prime = prime_factorize(A[i] // min_num)
    for j in prime:
        check[j] += 1
        
for i, j in check.items():
    if i == 2 or i == 3:
        ans += j
    else:
        print(-1)
        exit()

print(ans)