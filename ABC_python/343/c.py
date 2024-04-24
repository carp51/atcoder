N = int(input())

x = 10 ** 6 + 100

while True:
    if x ** 3 <= N:
        str_x = str(x ** 3)
        r_str_x = reversed(str_x,)
        if  list(str_x) == list(r_str_x):
            print(x ** 3)
            break
        
    x -= 1