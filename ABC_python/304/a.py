N = int(input())

min_num = 10 ** 20

SA = []

for i in range(N):
    S, A = map(str, input().split())
    min_num = min(min_num, int(A))
    SA.append([S, int(A)])
    
ans = []
SA *= 2

flag = False

for i in range(2 * N):
    if SA[i][1] == min_num:
        flag = True
    
    if not flag:
        continue
    
    ans.append(SA[i][0])
    
for i in ans[:N]:
    print(i)
    