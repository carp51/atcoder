from bisect import bisect_right


def is_prime(n):
    for i in range(2, n + 1):
        if i * i > n:
            break
        if n % i == 0:
            return False
    return n != 1


N = int(input())
s = [i for i in range(2, 10 ** 6 + 100) if is_prime(i)]

ans = 0

for i in range(len(s)):
    if s[i] == 2:
        continue
    
    tmp = N // pow(s[i], 3)
    tmp2 = bisect_right(s, tmp)
    
    if tmp2 == 0:
        break
    
    ans += min(i, tmp2)
    
print(ans)