import itertools


A, B, C = map(str, input().split())

A = list(A)
B = list(B)
C = int(C)
    
hatena_count = 0

for i in A:
    if i =="?":
        hatena_count += 1
        
for i in B:
    if i =="?":
        hatena_count += 1
        
all = itertools.product("0123456789", repeat=hatena_count)
for x in all:
    cnt = 0
    new_A = ""
    new_B = ""
    
    for i in range(len(A)):
        if A[i] == "?":
            new_A += x[cnt]
            cnt += 1
        else:
            new_A += A[i]
            
    for i in range(len(B)):
        if B[i] == "?":
            new_B += x[cnt]
            cnt += 1
        else:
            new_B += B[i]
    
    if int(new_A) * int(new_B) == C:
        for i in x:
            print(i)
            
        exit(0)