import heapq
import sys
from typing import List, Tuple, Final

# 무한대를 의미하는 상수 (충분히 큰 값)
INF: Final[int] = int(1e9)


def solve() -> None:
    # 빠른 입력을 위해 sys.stdin.readline 사용
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    v: int = int(input_data[0])  # 정점 개수
    e: int = int(input_data[1])  # 간선 개수
    start_node: int = int(input_data[2])  # 시작 정점

    # 인접 리스트로 그래프 구현
    graph: List[List[Tuple[int, int]]] = [[] for _ in range(v + 1)]
    
    idx = 3
    for _ in range(e):
        u: int = int(input_data[idx])
        target_v: int = int(input_data[idx + 1])
        w: int = int(input_data[idx + 2])
        graph[u].append((target_v, w))
        idx += 3

    # 최단 거리 테이블 초기화
    distance: List[int] = [INF] * (v + 1)
    
    # 다익스트라 알고리즘 수행
    dijkstra(start_node, graph, distance)

    # 결과 출력
    output = []
    for i in range(1, v + 1):
        if distance[i] == INF:
            output.append("INF")
        else:
            output.append(str(distance[i]))
    
    print("\n".join(output))


def dijkstra(start: int, graph: List[List[Tuple[int, int]]], distance: List[int]) -> None:
    """
    우선순위 큐를 이용한 다익스트라 알고리즘 구현
    """
    queue: List[Tuple[int, int]] = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여 큐에 삽입
    heapq.heappush(queue, (0, start))
    distance[start] = 0

    while queue:
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(queue)

        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue

        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for next_node, weight in graph[now]:
            cost = dist + weight
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(queue, (cost, next_node))


if __name__ == "__main__":
    solve()