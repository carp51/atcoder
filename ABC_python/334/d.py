from bisect import bisect_right

N, Q = map(int, input().split())
R = list(map(int, input().split()))

R.sort()

cs = [0]

for i in range(N):
    cs.append(cs[-1] + R[i])

for i in range(Q):
    q = int(input())
    print(bisect_right(cs, q) - 1)