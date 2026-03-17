import heapq
import sys
from typing import List, Dict

# 빠른 입력을 위해 사용
input = sys.stdin.readline


def dijkstra(start_node: int, graph: Dict[int, List[List[int]]], n: int) -> List[int]:
    """
    다익스트라 알고리즘을 사용하여 시작점에서 모든 노드까지의 최단 거리를 구함.
    """
    distances: List[int] = [float('inf')] * (n + 1)
    distances[start_node] = 0
    queue: List[List[int]] = [[0, start_node]]

    while queue:
        current_distance, current_destination = heapq.heappop(queue)

        if distances[current_destination] < current_distance:
            continue

        for new_destination, new_distance in graph[current_destination]:
            distance = current_distance + new_distance
            if distance < distances[new_destination]:
                distances[new_destination] = distance
                heapq.heappush(queue, [distance, new_destination])
    
    return distances


def solve() -> None:
    """
    테스트 케이스별로 문제를 해결하고 결과를 출력함.
    """
    line1 = input().split()
    if not line1:
        return
    n, m, t = map(int, line1)
    s, g, h = map(int, input().split())

    graph: Dict[int, List[List[int]]] = {i: [] for i in range(n + 1)}
    gh_weight: int = 0

    for _ in range(m):
        u, v, d = map(int, input().split())
        graph[u].append([v, d])
        graph[v].append([u, d])
        # g-h 사이의 간선 가중치를 저장해둠
        if (u == g and v == h) or (u == h and v == g):
            gh_weight = d

    candidates: List[int] = [int(input()) for _ in range(t)]

    # 1. 출발지 s에서 시작하는 다익스트라
    dist_s = dijkstra(s, graph, n)
    # 2. g에서 시작하는 다익스트라
    dist_g = dijkstra(g, graph, n)
    # 3. h에서 시작하는 다익스트라
    dist_h = dijkstra(h, graph, n)

    results: List[int] = []

    for cand in candidates:
        # 경로 1: s -> g -> h -> candidate
        path1 = dist_s[g] + gh_weight + dist_h[cand]
        # 경로 2: s -> h -> g -> candidate
        path2 = dist_s[h] + gh_weight + dist_g[cand]

        # s에서 candidate까지의 최단 거리가 path1 또는 path2와 같다면 가능성 있는 목적지
        if dist_s[cand] != float('inf'):
            if dist_s[cand] == path1 or dist_s[cand] == path2:
                results.append(cand)

    # 오름차순 정렬 후 출력
    results.sort()
    print(*(results))


if __name__ == "__main__":
    t_cases_str = input().strip()
    if t_cases_str:
        t_cases = int(t_cases_str)
        for _ in range(t_cases):
            solve()