from collections import Counter
import math
N = int(input())
a = list(map(int, input().split()))

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

min_num = a[0]

for i in range(1, N):
    min_num = math.gcd(min_num, a[i])

ans = 0

for i in range(N):
    if a[i] == 1:
        continue

    num = prime_factorize(a[i] // min_num)

    c = Counter(num)

    if c[2] + c[3] != len(num):
        print(-1)
        exit(0)
    
    ans += c[2] + c[3]

print(ans)