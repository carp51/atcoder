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

def is_prime(n):
    for i in range(2, n + 1):
        if i * i > n:
            break
        if n % i == 0:
            return False
    return n != 1

for i in range(T):
    t = int(input())

    flag = False
    for p in range(1, len(prime)):
        if not prime[p]:
            continue

        tmp = t / (p ** 2)

        if tmp.is_integer():
            if is_prime(int(tmp)):
                print(p, int(tmp))
                break

        tmp = t / p

        if tmp.is_integer():
            if is_prime(int(tmp) // 2):
                print(int(tmp) // 2, p)
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
