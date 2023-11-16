p, q = map(str, input().split())
A = [3, 1, 4, 1, 5, 9]

cs = [0]

for i in range(len(A)):
    cs.append(cs[-1] + A[i])
    
p = ord(p)
q = ord(q)

p, q = min(p, q), max(p, q)

print(cs[q - 65] - cs[p - 65])