def base_n(num_10,n):
    str_n = ''
    while num_10:
        if num_10%n>=10:
            return -1
        str_n += str(num_10%n)
        num_10 //= n
    return int(str_n[::-1])

N = int(input())

if N == 1:
    print(0)
    exit()

tmp = base_n(N - 1, 5)
    
print(tmp * 2)
