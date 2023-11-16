T = int(input())

for i in range(T):
    n = int(input())
    ans = 0
    a = list(map(int, input().split()))

    for j in range(n):
        if a[j] % 2 == 1:
            ans += 1

    print(ans)