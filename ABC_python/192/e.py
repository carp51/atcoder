import heapq


def Dijkstra(start):
    confirmed = [False] * (N + 1)
    
    time = [10 ** 20] * (N + 1)
    time[start] = 0 
    que = []
    
    heapq.heappush(que, [0, X])

    while 0 < len(que):
        now_time, now_city = heapq.heappop(que)
        
        # ここを入れてなかったので、TLE
        if confirmed[now_city]:
            continue
        
        confirmed[now_city] = True

        for to_city, T, K in connect[now_city]:
            if confirmed[to_city] == False:
                to_time = -(-now_time//K) * K + T
                if time[to_city] > to_time:
                    time[to_city] = to_time
                    heapq.heappush(que, [to_time, to_city])

    return time


N, M, X, Y = map(int, input().split())

connect = [[] for _ in range(N + 1)]

for i in range(M):
    A, B, T, K = map(int, input().split())
    connect[A].append([B, T, K])
    connect[B].append([A, T, K])

ans = Dijkstra(X)

print(ans[Y] if ans[Y] != 10 ** 20 else -1)