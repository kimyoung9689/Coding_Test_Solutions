import sys
from collections import deque
from typing import List, Dict

def solve() -> None:
    # 입력 받기
    input_data: List[int] = list(map(int, sys.stdin.readline().split()))
    if not input_data:
        return
    
    n, m, v = input_data
    
    # 인접 리스트 생성 (정점 번호가 작은 것부터 방문하기 위해 정렬 필요)
    graph: Dict[int, List[int]] = {i: [] for i in range(1, n + 1)}
    for _ in range(m):
        s, e = map(int, sys.stdin.readline().split())
        graph[s].append(e)
        graph[e].append(s)
    
    for key in graph:
        graph[key].sort()

    # DFS: 재귀 사용
    def dfs(curr: int, visited: List[bool]) -> None:
        visited[curr] = True
        print(curr, end=' ')
        for neighbor in graph[curr]:
            if not visited[neighbor]:
                dfs(neighbor, visited)

    # BFS: 큐 사용
    def bfs(start: int) -> None:
        visited: List[bool] = [False] * (n + 1)
        queue: deque = deque([start])
        visited[start] = True
        
        while queue:
            curr: int = queue.popleft()
            print(curr, end=' ')
            for neighbor in graph[curr]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)

    # 결과 출력
    dfs_visited: List[bool] = [False] * (n + 1)
    dfs(v, dfs_visited)
    print()
    bfs(v)

if __name__ == "__main__":
    solve()