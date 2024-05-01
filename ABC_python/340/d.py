import heapq


def Dijkstra(start):
    confirmed = [False] * (N + 1)
    
    time = [10 ** 20] * (N + 1)
    time[start] = 0 
    que = []
    
    heapq.heappush(que, [0, start])

    while 0 < len(que):
        now_time, now_city = heapq.heappop(que)
        
        # ここを入れてなかったので、TLE
        if confirmed[now_city]:
            continue
        
        confirmed[now_city] = True

        for to_city, T in connect[now_city]:
            if confirmed[to_city] == False:
                to_time = now_time + T
                if time[to_city] > to_time:
                    time[to_city] = to_time
                    heapq.heappush(que, [to_time, to_city])

    return time


N = int(input())

connect = [[] for _ in range(N + 1)]

for i in range(1, N):
    A, B, X = map(int, input().split())
    connect[i].append([i + 1, A])
    connect[i].append([X, B])

ans = Dijkstra(1)

print(ans[-1])