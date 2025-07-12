import heapq

def dijkstra(graph, start):
    """
    ダイクストラ法で最短経路を計算する関数

    Args:
        graph (dict): グラフの隣接リスト表現
                      例: {'A': {'B': 1, 'C': 4}, 'B': {'A': 1, 'C': 2, 'D': 5}, ...}
        start (any): 開始ノード

    Returns:
        dict: 開始ノードから各ノードへの最短距離
    """
    # 各ノードへの最短距離を無限大で初期化
    distances = {node: float('inf') for node in graph}
    # 開始ノードの距離は0
    distances[start] = 0

    # 優先度付きキュー。(距離, ノード)のタプルを格納
    priority_queue = [(0, start)]

    while priority_queue:
        # 現在の最短距離が最も小さいノードを取り出す
        current_distance, current_node = heapq.heappop(priority_queue)

        # 既に処理済みのノード（より短い経路が見つかっている場合）はスキップ
        if current_distance > distances[current_node]:
            continue

        # 隣接ノードへの距離を更新
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # より短い経路が見つかった場合
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                # 優先度付きキューに新しい距離とノードを追加
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# --- 実行例 ---
if __name__ == '__main__':
    # グラフの定義（重み付き有向グラフ）
    # ノード 'A' から 'B' へのコストが 1、'A' から 'C' へのコストが 4 という意味
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1}
    }

    # 開始ノードを指定
    start_node = 'A'

    # ダイクストラ法を実行
    shortest_distances = dijkstra(graph, start_node)

    # 結果の表示
    print(f"開始ノード '{start_node}' からの最短距離:")
    for node, distance in shortest_distances.items():
        print(f"  {node} まで: {distance}")