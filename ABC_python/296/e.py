from bisect import bisect_right
N, M = map(int, input().split())

l = [i for i in range(1, int(M ** 0.5) + 100)]

ans = 10 ** 20

for i in l:
    tmp = bisect_right(l, )