import sys, time
from collections import defaultdict

def enter_time_comparison(date1, date2, time2, date3):
    x = date1
    y = date2 + " " + time2
    z = date3
    x = "".join(x)
    z = "".join(z)
    first = time.strptime(x, "%Y/%m/%d %H:%M:%S")
    second = time.strptime(y, "%Y/%m/%d %H:%M:%S")
    third  = time.strptime(z, "%Y/%m/%d %H:%M:%S")
    return first <= second <= third

def issue_time_comparison(date1, time1, date2, time2):
    x = date1 + " " + time1
    y = date2 + " " + time2
    x = "".join(x)
    y = "".join(y)
    first = time.strptime(x, "%Y/%m/%d %H:%M:%S")
    second = time.strptime(y, "%Y/%m/%d %H:%M:%S")
    return first <= second

def main(lines):
    id_check_list = defaultdict(int)
    guest_id_check_list = defaultdict(lambda: [0, 0, "", "", 0])
    date, time = "2000/01/21", "00:00:00"
    if lines[0] == "1":
        for i in range(2, 2 + int(lines[1])):
            id_check_list[lines[i]] = 1
        
        for i in range(2 + int(lines[1]), len(lines)):
            query = list(map(str, lines[i].split()))
            if query[0] == "enter":
                date, time, id = query[1], query[2], query[3]
                if id_check_list[id] == 1:
                    print("can")
                else:
                    print("cannot")
            elif query[0] == "issue":
                id = query[1]
                id_check_list[id] = 1
            elif query[0] == "disable":
                id = query[1]
                id_check_list[id] = 0
    elif lines[0] == "2":
        for i in range(1, len(lines)):
            query = list(map(str, lines[i].split()))
            if query[0] == "enter":
                date, time, id = query[1], query[2], query[3]
                if guest_id_check_list[id][0] == 0:
                    print("unissued id")
                elif guest_id_check_list[id][1] == 0:
                    print("disabled id")
                elif  not enter_time_comparison(guest_id_check_list[id][2], date, time, guest_id_check_list[id][3]):
                    print("not applicable now")
                else:
                    print("can")
                    guest_id_check_list[id][4] = 1

            elif query[0] == "issue":
                id, date1, time1, date2, time2 = query[1], query[2], query[3], query[4], query[5]
                if not issue_time_comparison(date1, time1, date2, time2):
                    print("invalid info")
                elif not issue_time_comparison(date, time, date2, time2):
                    print("invalid info")
                else:
                    print("successfully issued")
                    guest_id_check_list[id][0], guest_id_check_list[id][1], guest_id_check_list[id][2], guest_id_check_list[id][3] = 1, 1, date1 + " " + time1, date2 + " " + time2
                    
            elif query[0] == "update":
                id, date1, time1, date2, time2 = query[1], query[2], query[3], query[4], query[5]
                if not issue_time_comparison(date1, time1, date2, time2):
                    print("invalid info")
                elif not issue_time_comparison(date, time, date2, time2):
                    print("invalid info")
                elif guest_id_check_list[id][4] == 1:
                    print("already used")
                else:
                    print("successfully updated")
                    guest_id_check_list[id][0], guest_id_check_list[id][1], guest_id_check_list[id][2], guest_id_check_list[id][3] = 1, 1, date1 + " " + time1, date2 + " " + time2
                           
            elif query[0] == "disable":
                id = query[1]
                if guest_id_check_list[id][4] == 1:
                    print("already used")
                else:
                    print("successfully disabled")
                    guest_id_check_list[id][1], guest_id_check_list[id][2], guest_id_check_list[id][3] = 0, "", ""
                
                
"""             
if __name__ == '__main__':
    lines = []
    for l in sys.stdin:
        lines.append(l.rstrip('\r\n'))
    main(lines)
"""


if __name__ == '__main__':
    lines = []
    for l in range(9):
        s = input()
        lines.append(s)
    main(lines)