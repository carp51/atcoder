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

count = 0
for A in range(1, N+1):
    for B in range(1, N+1):
        if A*B >= N:
            break
    
        if len(make_divisors(N - A * B)) % 2 == 0:
            count += (len(make_divisors(N - A * B)) // 2) * 2
        else:
            count += ((len(make_divisors(N - A * B))) // 2) * 2 + 1
        

print(count)
