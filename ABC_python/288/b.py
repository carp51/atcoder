N, K = map(int, input().split())
l = []

for i in range(N):
    S = input()
    l.append(S)

l = l[:K]
l.sort()

for i in l:
    print(i)
