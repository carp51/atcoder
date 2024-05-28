from collections import defaultdict

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


K = int(input())
check = defaultdict(int)

for i in prime_factorize(K):
    check[i] += 1
    
for i in range(1, 10000000):
    for j in prime_factorize(i):
        check[j] -= 1
     
    flag = True   
    for k in check.values():
        if k > 0:
            flag = False
    
    if flag:
        print(i)
        exit()