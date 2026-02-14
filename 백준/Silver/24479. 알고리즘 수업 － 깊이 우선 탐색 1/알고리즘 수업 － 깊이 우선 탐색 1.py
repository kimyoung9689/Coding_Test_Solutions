import sys
from typing import List

# 재귀 한도 늘리기 (DFS 필수)
sys.setrecursionlimit(200000)

def solve() -> None:
    # 빠른 입력을 위해 사용
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n: int = int(input_data[0])  # 정점 수
    m: int = int(input_data[1])  # 간선 수
    r: int = int(input_data[2])  # 시작 정점

    # 인접 리스트 생성
    graph: List[List[int]] = [[] for _ in range(n + 1)]
    idx: int = 3
    for _ in range(m):
        u: int = int(input_data[idx])
        v: int = int(input_data[idx + 1])
        graph[u].append(v)
        graph[v].append(u)
        idx += 2

    # 1. 인접 정점 오름차순 정렬
    for i in range(1, n + 1):
        graph[i].sort()

    visited: List[int] = [0] * (n + 1)
    order: int = 1

    def dfs(current_node: int) -> None:
        nonlocal order
        visited[current_node] = order  # 현재 노드에 방문 순서 저장
        
        for neighbor in graph[current_node]:
            if visited[neighbor] == 0:
                order += 1
                dfs(neighbor)

    # DFS 시작
    dfs(r)

    # 결과 출력 (1번 정점부터 n번 정점까지 순서대로)
    print('\n'.join(map(str, visited[1:])))

if __name__ == "__main__":
    solve()