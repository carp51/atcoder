H_A, W_A = map(int, input().split())
A = [list(input()) for _ in range(H_A)]

H_B, W_B = map(int, input().split())
B = [list(input()) for _ in range(H_B)]

H_C, W_C = map(int, input().split())
C = [list(input()) for _ in range(H_C)]

N_A = len(A)

while True:
    if "#" in A[N_A - 1]:
        break
    else:
        N_A -= 1
    
A = A[:N_A]   
        
cnt = 0
while True:
    if "#" in A[cnt]:
        break
    else:
        cnt += 1
        
A = A[cnt:]

transposed_matrix = [list(x) for x in zip(*A)]

N_A = len(transposed_matrix)

while True:
    if "#" in transposed_matrix[N_A - 1]:
        break
    else:
        N_A -= 1
    
transposed_matrix = transposed_matrix[:N_A]   
        
cnt = 0
while True:
    if "#" in transposed_matrix[cnt]:
        break
    else:
        cnt += 1
        
transposed_matrix = transposed_matrix[cnt:]

A = [list(x) for x in zip(*transposed_matrix)]



N_B = len(B)

while True:
    if "#" in B[N_B - 1]:
        break
    else:
        N_B -= 1
    
B = B[:N_B]   
        
cnt = 0
while True:
    if "#" in B[cnt]:
        break
    else:
        cnt += 1
        
B = B[cnt:]

transposed_matrix = [list(x) for x in zip(*B)]

N_B = len(transposed_matrix)

while True:
    if "#" in transposed_matrix[N_B - 1]:
        break
    else:
        N_B -= 1
    
transposed_matrix = transposed_matrix[:N_B]   
        
cnt = 0
while True:
    if "#" in transposed_matrix[cnt]:
        break
    else:
        cnt += 1
        
transposed_matrix = transposed_matrix[cnt:]

B = [list(x) for x in zip(*transposed_matrix)]



N_C = len(C)

while True:
    if "#" in C[N_C - 1]:
        break
    else:
        N_C -= 1
    
C = C[:N_C]   
        
cnt = 0
while True:
    if "#" in C[cnt]:
        break
    else:
        cnt += 1
        
C = C[cnt:]

transposed_matrix = [list(x) for x in zip(*C)]

N_C = len(transposed_matrix)

while True:
    if "#" in transposed_matrix[N_C - 1]:
        break
    else:
        N_C -= 1
    
transposed_matrix = transposed_matrix[:N_C]   
        
cnt = 0
while True:
    if "#" in transposed_matrix[cnt]:
        break
    else:
        cnt += 1
        
transposed_matrix = transposed_matrix[cnt:]

C = [list(x) for x in zip(*transposed_matrix)]

H_A, W_A = len(A), len(A[0])
H_B, W_B = len(B), len(B[0])
H_C, W_C = len(C), len(C[0])

X = [["."] * W_C for _ in range(H_C)]

for i in range(H_C - H_A + 1):
    for j in range(W_C - W_A + 1):
        for k in range(H_C - H_B + 1):
            for l in range(W_C - W_B + 1):
                for a in range(H_A):
                    for b in range(W_A):
                        X[i + a][j + b] = A[a][b]
                
                for a in range(H_B):
                    for b in range(W_B):
                        if X[k + a][l + b] == "#":
                            continue
                        X[k + a][l + b] = B[a][b]
                        
                if X == C:
                    print("Yes")
                    exit(0)
                    
                X = [["."] * W_C for _ in range(H_C)]
        
print("No")        