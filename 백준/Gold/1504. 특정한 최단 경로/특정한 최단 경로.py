import heapq
import sys
from typing import List, Dict

# 빠른 입력을 위해 사용해
input = sys.stdin.readline
INF: int = int(1e9)


def dijkstra(start: int, n: int, graph: List[List[Dict[str, int]]]) -> List[int]:
    """
    다익스트라 알고리즘을 사용하여 시작 정점으로부터 모든 정점까지의 최단 거리를 구해.
    """
    distances: List[int] = [INF] * (n + 1)
    distances[start] = 0
    queue: List[tuple] = [(0, start)]

    while queue:
        current_dist, current_node = heapq.heappop(queue)

        if distances[current_node] < current_dist:
            continue

        for neighbor in graph[current_node]:
            target_node: int = neighbor['node']
            weight: int = neighbor['dist']
            new_dist: int = current_dist + weight

            if new_dist < distances[target_node]:
                distances[target_node] = new_dist
                heapq.heappush(queue, (new_dist, target_node))

    return distances


def solve() -> None:
    # 정점 개수 N, 간선 개수 E 입력
    try:
        line1 = input().split()
        if not line1:
            return
        n, e = map(int, line1)
    except ValueError:
        return

    graph: List[List[Dict[str, int]]] = [[] for _ in range(n + 1)]

    # 간선 정보 입력 (양방향)
    for _ in range(e):
        u, v, w = map(int, input().split())
        graph[u].append({'node': v, 'dist': w})
        graph[v].append({'node': u, 'dist': w})

    # 반드시 거쳐야 하는 두 정점
    v1, v2 = map(int, input().split())

    # 필요한 최단 거리들을 구해 (1에서 시작, v1에서 시작, v2에서 시작)
    dist_from_1 = dijkstra(1, n, graph)
    dist_from_v1 = dijkstra(v1, n, graph)
    dist_from_v2 = dijkstra(v2, n, graph)

    # 경로 1: 1 -> v1 -> v2 -> n
    path1: int = dist_from_1[v1] + dist_from_v1[v2] + dist_from_v2[n]
    # 경로 2: 1 -> v2 -> v1 -> n
    path2: int = dist_from_1[v2] + dist_from_v2[v1] + dist_from_v1[n]

    result: int = min(path1, path2)

    # 경로가 없는 경우 처리
    if result >= INF:
        print("-1")
    else:
        print(result)


if __name__ == "__main__":
    solve()