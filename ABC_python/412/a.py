N = int(input())

cnt = 0

for i in range(N):
    A, B = map(int, input().split())
    if B > A:
        cnt += 1
        
print(cnt)