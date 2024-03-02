from collections import defaultdict

K = int(input())


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

check = defaultdict(int)

n = prime_factorize(K)

for i in range(len(n)):
    check[n[i]] += 1

ans = -10

for i, j in check.items():
    count = 0

    while j > 0:
        count += 1
        tmp = prime_factorize(i * count)
        ans = max(ans, i * count)
        j -= tmp.count(i)

print(ans)