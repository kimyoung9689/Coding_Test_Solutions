import sys
from collections import deque
from typing import List, Deque

# 빠른 입력을 위해 사용
input = sys.stdin.readline


def is_bipartite(v_count: int, adj: List[List[int]]) -> str:
    """
    주어진 그래프가 이분 그래프인지 판별하는 함수
    """
    # 0: 미방문, 1: 빨강, 2: 파랑
    colors: List[int] = [0] * (v_count + 1)

    for i in range(1, v_count + 1):
        if colors[i] != 0:
            continue

        # BFS 시작
        queue: Deque[int] = deque([i])
        colors[i] = 1

        while queue:
            curr: int = queue.popleft()

            for neighbor in adj[curr]:
                if colors[neighbor] == 0:
                    # 아직 안 가본 곳은 반대 색으로 칠함
                    colors[neighbor] = 3 - colors[curr]
                    queue.append(neighbor)
                elif colors[neighbor] == colors[curr]:
                    # 인접한 노드가 같은 색이면 이분 그래프 아님
                    return "NO"
    
    return "YES"


def solve() -> None:
    """
    메인 실행 함수
    """
    try:
        line = input().strip()
        if not line:
            return
        k: int = int(line)
    except ValueError:
        return

    for _ in range(k):
        v, e = map(int, input().split())
        adj: List[List[int]] = [[] for _ in range(v + 1)]
        
        for _ in range(e):
            u, v_node = map(int, input().split())
            adj[u].append(v_node)
            adj[v_node].append(u)
        
        print(is_bipartite(v, adj))


if __name__ == "__main__":
    solve()