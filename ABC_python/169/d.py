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

cnt = 0

num_list = prime_factorize(N)
num_list = list(set(num_list))
num_list.sort()

for p in num_list:
    for e in range(1, 10 ** 6):
        z = p ** e
        if z > N:
            break
        
        if N % z == 0:
            cnt += 1
            N //= z
        else:
            break
    
    

print(cnt)