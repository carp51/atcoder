import copy
T = int(input())

for i in range(T):
    N = int(input())
    S = list(map(int, input().split()))
    new_S = copy.copy(S)

    new_S = list(new_S[1:-1])
    new_S.sort()
    
    first_val, second_val = S[0], S[-1]
    
    if 2 * first_val >= second_val:
        print(2)
        continue
        
    cnt = 1
    
    while True:
        candidate = [i for i in new_S if i <= 2 * first_val]
        if len(candidate) == 0:
            print(-1)
            break
        
        max_candidate = max(candidate)
        first_val = max_candidate
        cnt += 1
        new_S.remove(max_candidate)
        
        if 2 * max_candidate >= second_val:
            print(cnt + 1)
            break
        