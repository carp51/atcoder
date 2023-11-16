def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort()
    return divisors

N = int(input())

s = set()

for i in range(N):
    n = int(input())
    
    yakusuu = set(make_divisors(n))
    
    if i == 0:
        s = s | yakusuu
    else:
        s = s & yakusuu
        
s = list(s)
s.sort()

print(s[-1])