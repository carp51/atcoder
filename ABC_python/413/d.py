T = int(input())

def is_integer_num(n):
    if isinstance(n, int):
        return True
    if isinstance(n, float):
        return n.is_integer()
    return False

for i in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    sort_A = []
    check_A = []

    
    new_A = []
    for j in range(N):
        if A[j] < 0:
            new_A.append([-A[j], -1])
            check_A.append(-A[j])
        else:
            new_A.append([A[j], 1])
            check_A.append(A[j])
            
    new_A.sort()
    
    if len(set(check_A)) == 1:
        plus_count, minus_count = 0, 0
        for k in range(N):
            if A[k] > 0:
                plus_count += 1
            else:
                minus_count += 1
                
        if N % 2 == 0:
            if plus_count == minus_count or plus_count == N or minus_count == N:
                print("Yes")
            else:
                print("No")
        else:
            if abs(plus_count - minus_count) == 1 or plus_count == N or minus_count == N:
                print("Yes")
            else:
                print("No")
        continue
    
    for j in range(N):
        sort_A.append(new_A[j][0] * new_A[j][1])
        
    flag = False
        
    for j in range(N - 2):
        left_nums = [sort_A[j], sort_A[j + 1]]
        right_nums = [sort_A[j + 1], sort_A[j + 2]]
        if left_nums[1] * right_nums[0] != left_nums[0] * right_nums[1]:
            print("No")
            flag = True
            break
    
    # for j in range(N - 2):
    #     left_nums = [new_A[j], new_A[j + 1]]
    #     right_nums = [new_A[j + 1], new_A[j + 2]]
    #     print(left_nums[1]/left_nums[0], right_nums[1]/right_nums[0])
    #     if (left_nums[1]/left_nums[0]) != (right_nums[1]/right_nums[0]):
    #         print("No")
    #         break
        
    if flag == False:
        print("Yes")
    
    # rate = new_A[1] / new_A[0]
    
    # first_num = -1
    
    # for j in range(N):
    #     if new_A[0] == A[j] or -new_A[0] == A[j]:
    #         first_num = A[j]
    #         break
    
    # plus_A, minus_A = [first_num], [first_num]
    
    # for j in range(N - 1):
    #     if not is_integer_num((plus_A[-1] * rate)) or not is_integer_num(minus_A[-1] * (-rate)):
    #         plus_A.append(-10 * 20)
    #         minus_A.append(10 ** 20)
    #         break
        
    #     plus_A.append(int(plus_A[-1] * rate))
    #     minus_A.append(int(minus_A[-1] * (-rate)))
        
    # A.sort()
    # plus_A.sort()
    # minus_A.sort()
    
    # if A == plus_A or A == minus_A:
    #     print("Yes")
    # else:
    #     print("No")