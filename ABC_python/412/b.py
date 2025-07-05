S = input()
T = input()

# first_index = -1
# second_index = -1
# cnt = 0

# for i in range(len(S)):
#     if S[i].isupper():
#         if cnt == 0:
#             first_index = i
#             cnt += 1
#         elif cnt == 1:
#             second_index = i
#             cnt += 1
            
# if first_index != -1 and second_index != -1:
#     print("Yes" if S[second_index - 1] in T else "No")
    
# if first_index == -1:
#     print("Yes")

# if second_index == -1:
    
for i in range(1, len(S)):
    if S[i].islower():
        continue
    
    if S[i - 1] not in T:
        print("No")
        exit()
            
print("Yes")