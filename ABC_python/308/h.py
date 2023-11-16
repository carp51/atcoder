import time
 

 
x = "2011/04/06 04:06:30"
y = "2011/04/06 04:06:29"
 
first = time.strptime(x, "%Y/%m/%d %H:%M:%S")
second = time.strptime(y, "%Y/%m/%d %H:%M:%S")
 
if first < second:
    print('First date is less than the second date.')
elif first > second:
    print('First date is more than the second date.')
else:
    print('Both dates are the same.')
    
def enter_time_comparison(date1, time1, date2, time2, date3, time3):
    x = date1 + [" "] + time1
    y = date2 + [" "] + time2
    z = date3 + [" "] + time3
    x = "".join(x)
    y = "".join(y)
    z = "".join(z)
    first = time.strptime(x, "%Y/%m/%d %H:%M:%S")
    second = time.strptime(y, "%Y/%m/%d %H:%M:%S")
    third  = time.strptime(z, "%Y/%m/%d %H:%M:%S")
    return first <= second <= third

def issue_time_comparison(date1, time1, date2, time2):
    x = date1 + [" "] + time1
    y = date2 + [" "] + time2
    x = "".join(x)
    y = "".join(y)
    first = time.strptime(x, "%Y/%m/%d %H:%M:%S")
    second = time.strptime(y, "%Y/%m/%d %H:%M:%S")
    return first <= second
time_comparison(["2011/04/06"], ["04:06:30"], ["2011/04/06"], ["04:06:30"])