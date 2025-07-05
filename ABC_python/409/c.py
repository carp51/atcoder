from collections import defaultdict


N, L = map(int, input().split())
d = list(map(int, input().split()))

check_num = [3 * 2 ** i for i in range(50)]

# if L not in check_num:
#     print(0)
#     exit()

if L % 3 != 0:
    print(0)
    exit()
    
cnt = 0

check = defaultdict(int)


cs = [0]

for i in range(N - 1):
    cs.append(cs[-1] + d[i])
    
for i in cs:
    check[i % L] += 1
    
for i in range(L // 3):
    left_cnt = check[i + L // 3 * 2]
    righ_cnt = check[i + L // 3]
    now_cnt = check[i]
    
    cnt += now_cnt * righ_cnt * left_cnt

print(cnt)