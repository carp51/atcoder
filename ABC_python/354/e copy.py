def main():
    
    n = int(input())
    a = []
    b = []
    index = 1
    
    for i in range(n):
        A, B = map(int, input().split())
        a.append(A)
        b.append(B)
        index += 2
    
    dp = [-1] * (1 << n)
    dp[0] = 0
    
    for i in range(1, (1 << n)):
        f = False
        for j in range(n):
            for k in range(j + 1, n):
                if (i & (1 << j)) and (i & (1 << k)):
                    if (a[j] == a[k] or b[j] == b[k]) and dp[i ^ (1 << j) ^ (1 << k)] == 0:
                        f = True
        dp[i] = 1 if f else 0
    
    print("Takahashi" if dp[-1] else "Aoki")

if __name__ == "__main__":
    main()
