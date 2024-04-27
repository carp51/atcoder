from bisect import bisect_right

L, R = map(int, input().split())

a_2 = [2 ** i for i in range(61)]

ans = []

while L < R:
    index = bisect_right(a_2, L)
    if L == 0:
        index = bisect_right(a_2, R)
    while index >= 0:
        index -= 1
        if L % a_2[index] != 0:
            continue
        
        if a_2[index] * (L // a_2[index] + 1) <= R:
            break
       
    ans.append([L, a_2[index] * (L // a_2[index] + 1)])
    L = a_2[index] * (L // a_2[index] + 1)
        
print(len(ans))
for i in ans:
    print(*i)    