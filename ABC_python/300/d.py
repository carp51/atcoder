from bisect import bisect_right

# 1 以上 N 以下の整数が素数かどうかを返す
def Eratosthenes(N):
    # テーブル
    isprime = [True] * (N+1)

    # 0, 1 は予めふるい落としておく
    isprime[0], isprime[1] = False, False

    # ふるい
    for p in range(2, N+1):
        # すでに合成数であるものはスキップする
        if not isprime[p]:
            continue

        # p 以外の p の倍数から素数ラベルを剥奪
        q = p * 2
        while q <= N:
            isprime[q] = False
            q += p

    # 1 以上 N 以下の整数が素数かどうか
    return isprime

# 50 以下の素数をすべて求める
isprime = Eratosthenes(10 ** 6 + 2000)

N = int(input())

s = [i for i in range(len(isprime)) if isprime[i]]
ss = [i * i for i in s]

n = 2000

ans = 0

for a in range(n):
    for b in range(a + 1, n):
        c = N / s[a] ** 2
        c = c / s[b]
        c = int(c)
        
        tmp =  bisect_right(ss, c) - bisect_right(ss, max(s[a] ** 2, s[b] ** 2))
        
        if tmp > 0:
            ans += tmp
    
            
print(ans)