N = int(input())
H = list(map(int, input().split()))

for h in range(N):
    if H[h] > H[0]:
        print(h + 1)
        exit()
        
print(-1)