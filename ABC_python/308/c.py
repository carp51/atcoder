from functools import cmp_to_key

def cmp(a, b):  # a = [x_a, y_a, index_a], b = [x_b, y_b, index_b]
    if a[0] * b[1] == b[0] * a[1]:
        return b[2] - a[2] 
    # a, bという順で並んでほしい条件のときは-1を返し、それ以外では1を返す
    return -1 if a[0] * b[1] < b[0] * a[1] else 1

N = int(input())

l = []

for i in range(N):
    A, B = map(int, input().split())
    l.append([A, A + B, i + 1])
    
l = sorted(l, key=cmp_to_key(cmp))


ans = []

for A in l:
    ans.append(A[2])
    
ans.reverse()
    
print(*ans)
