import sys
from typing import List, Dict


def solve() -> None:
    # 입력 처리
    try:
        line1 = sys.stdin.readline()
        if not line1:
            return
        n: int = int(line1.strip())
        
        line2 = sys.stdin.readline()
        if not line2:
            return
        m: int = int(line2.strip())
    except ValueError:
        return

    # 인접 리스트 초기화
    adj: Dict[int, List[int]] = {i: [] for i in range(1, n + 1)}
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].append(v)
        adj[v].append(u)

    # 방문 여부 체크
    visited: List[bool] = [False] * (n + 1)
    
    # DFS 함수
    def dfs(curr: int) -> None:
        visited[curr] = True
        for neighbor in adj[curr]:
            if not visited[neighbor]:
                dfs(neighbor)

    # 1번 컴퓨터부터 시작
    dfs(1)

    # 1번을 제외하고 감염된 컴퓨터 수 계산
    result: int = sum(1 for i in range(2, n + 1) if visited[i])
    print(result)


if __name__ == "__main__":
    solve()