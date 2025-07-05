# import random  
# import itertools
# def f():
#     random_val = []
    
#     for i in range(7):
#         random_val.append(chr(random.randrange(97, 123)))
        
#     return "".join(random_val)

# def ans_val(random_val):
#     random_val = list(random_val)
#     check = []
#     for v in itertools.permutations(random_val, 7):
#         check.append("".join(v))
        
#     check.sort()
#     return check[0]

# T = int(input())
# for i in range(T):
#     N = int(input())
#     S = input()
    
#     first_val = "a"
#     target_val = "zzzzzzzzzzzz"
#     first_index = 0
#     last_index = N - 1
#     flag = False
    
#     ans = []
    
#     for i in range(N):
#         if first_val > S[i] and (not flag):
#             flag = True
#             target_val = first_val
#             first_index = i
#             ans.pop()
        
#         first_val = S[i]
        
#         if target_val < S[i]:
#             last_index = i
#             ans.append(target_val)
#             for j in range(i, N):
#                 ans.append(S[j])
#             break
        
#         ans.append(S[i])
        
#     if len(ans) == N - 1 and target_val != "zzzzzzzzzzzz":
#         ans.append(target_val)
        
#     print("".join(ans))   

T = int(input())
for i in range(T):
    N = int(input())
    S = input()
    
    if N == 1:
        print(S)
        continue
    
    first_index = -1
    for j in range(N - 1):
        if S[j] > S[j + 1]:
            first_index = j
            break
        
    last_index = N
    for j in range(first_index, N):
        if S[j] > S[first_index]:
            last_index = j
            break
            
    if first_index == -1:
        print(S)
    else:
        print(S[:first_index] + S[first_index + 1: last_index ]+ S[first_index] + S[last_index :])
        # print(S[:first_index] , S[first_index + 1: last_index ], S[first_index] ,S[last_index :])