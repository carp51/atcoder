Q = int(input())

q = [list(map(int, input().split())) for i in range(Q)]
q.insert(0, [1, 1])

S = ""

check = []
two_cnt = 0


for i in range(Q + 1):
    if q[i][0] == 2:
        two_cnt += 1
    elif q[i][0] == 3:
        check.append(two_cnt)
        two_cnt = 0
        
check.append(two_cnt)
        
three_count = 0
cnt = 0

for i in range(Q + 1):
    if q[i][0] == 1:
        if check[three_count] > cnt:
            continue
        else:
            S += str(q[i][1])
    elif q[i][0] == 3:
        ans = pow(int(S), 1, 998244353)
        print(ans)