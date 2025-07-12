N, M = map(int, input().split())
A = list(map(int, input().split()))

sum = sum(A)

print("Yes" if sum <= M else "No")