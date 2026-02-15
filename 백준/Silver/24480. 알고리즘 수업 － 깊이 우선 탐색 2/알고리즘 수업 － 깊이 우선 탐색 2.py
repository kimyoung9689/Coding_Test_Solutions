import sys

# 파이썬 기본 재귀 한도는 낮아서 늘려줘야 해
sys.setrecursionlimit(200000)

def solve() -> None:
    # 빠른 입력을 위해 사용해
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n: int = int(input_data[0])  # 정점 수
    m: int = int(input_data[1])  # 간선 수
    r: int = int(input_data[2])  # 시작 정점

    # 인접 리스트 생성
    adj: list[list[int]] = [[] for _ in range(n + 1)]
    ptr: int = 3
    for _ in range(m):
        u: int = int(input_data[ptr])
        v: int = int(input_data[ptr + 1])
        adj[u].append(v)
        adj[v].append(u)
        ptr += 2

    # 문제 조건: 인접 정점을 내림차순으로 방문
    for i in range(1, n + 1):
        adj[i].sort(reverse=True)

    visited_order: list[int] = [0] * (n + 1)
    current_order: int = 1

    def dfs(node: int) -> None:
        nonlocal current_order
        visited_order[node] = current_order
        
        for neighbor in adj[node]:
            if visited_order[neighbor] == 0:
                current_order += 1
                dfs(neighbor)

    # DFS 시작
    dfs(r)

    # 결과 출력 (1번 정점부터 N번 정점까지 순서대로)
    print('\n'.join(map(str, visited_order[1:])))

if __name__ == "__main__":
    solve()