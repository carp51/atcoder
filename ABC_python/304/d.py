from bisect import bisect_right

W, H = map(int, input().split())
N = int(input())
pq = []

for i in range(N):
    p, q = map(int, input().split())
    pq.append([p, q])
    
A = int(input())
a = list(map(int, input().split()))
B = int(input())
b = list(map(int, input().split()))

a.append(10 ** 20)
b.append(10 ** 20)

pq.sort()

A_list = []
A_num = 0
tmp = []
i = 0

while i < N:
    if pq[i][0] <= a[A_num]:
        tmp.append(pq[i][1])
        i += 1
    else:
        A_list.append(tmp)
        tmp = []
        A_num += 1
        
A_list.append(tmp)

min_num = 10 ** 20
max_num = -10
        
for w in A_list:
    w.sort()
    
    
    
    
print(min_num, max_num)