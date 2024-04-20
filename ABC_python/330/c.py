from bisect import bisect_right

D = int(input())

a_2 = [i ** 2 for i in range(0, 2 * 10 ** 6 + 1000)]

ans = 10 ** 20

for x_2 in a_2:
    y_2 = D - x_2
    
    index = bisect_right(a_2, y_2)
    
    ans = min(ans, abs(a_2[index] - y_2))
    ans = min(ans, abs(a_2[index - 1] - y_2))
    
print(ans)