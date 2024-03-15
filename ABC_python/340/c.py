N = int(input())
ans = 0
i = 0

while N >= 2:
    ans += N * (2 ** i)
    N //= 2
    
print(ans)
    