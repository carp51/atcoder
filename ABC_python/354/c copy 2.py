N = int(input())
AC = []
for i in range(N):
    A, C = map(int, input().split())
    AC.append([C, A, i])
    
AC.sort()
num = 0
check = []

for i in range(N):
    if AC[i][1] >= num:
        num = AC[i][1]
        check.append(AC[i][2] + 1)
    else:
        continue
check.sort()
print(len(check))
print(*check)