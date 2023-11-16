def eratosthenes(n):
    is_prime = [False, False] + [True] * (n-1)
    for p in range(2, n+1):
        if not(is_prime[p]):
            continue
        for k in range(p*2, n+1, p):
            is_prime[k] = False
    return is_prime

prime = eratosthenes(10 ** 6 * 3 + 100)

ans = []

T = int(input())

for i in range(T):
    t = int(input())

    flag = False
    for p in range(1, len(prime) - 1):
        if not prime[p]:
            continue

        tmp = t / (p ** 2)

        if t % p ** 2 == 0 and tmp * p ** 2 == t and tmp != p:
            print(p, int(tmp))
            flag = True
            break

    if flag:
        continue

    for q in range(1, len(prime) - 1):
        if not prime[q]:
            continue

        tmp = t / q

        if t % q == 0 and tmp * q == t and (int(tmp) // 2) != q:
            print(int(tmp) // 2, q)
            break


    

    








"""
T = int(input())

for i in range(T):
    t = int(input())

    check = prime_factorize(t)
    check.sort()

    if check.count(check[0]) == 1:
        print(check[-1], check[0])
    else:
        print(check[0], check[-1])
"""
