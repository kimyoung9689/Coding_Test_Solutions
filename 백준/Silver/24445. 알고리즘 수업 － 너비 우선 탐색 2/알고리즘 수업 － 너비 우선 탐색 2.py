import sys
from collections import deque
from typing import List, Deque

def solve() -> None:
    # 빠른 입력을 위해 sys.stdin.readline 사용
    input_data: List[str] = sys.stdin.read().split()
    if not input_data:
        return

    n: int = int(input_data[0])  # 정점 수
    m: int = int(input_data[1])  # 간선 수
    r: int = int(input_data[2])  # 시작 정점

    # 인접 리스트 생성
    adj: List[List[int]] = [[] for _ in range(n + 1)]
    cursor: int = 3
    for _ in range(m):
        u: int = int(input_data[cursor])
        v: int = int(input_data[cursor + 1])
        adj[u].append(v)
        adj[v].append(u)
        cursor += 2

    # 문제 조건: 인접 정점은 내림차순으로 방문
    for i in range(1, n + 1):
        adj[i].sort(reverse=True)

    # 방문 순서 저장 배열 (0으로 초기화)
    visited_order: List[int] = [0] * (n + 1)
    order: int = 1
    
    # BFS 탐색
    queue: Deque[int] = deque([r])
    visited_order[r] = order
    
    while queue:
        curr: int = queue.popleft()
        
        for neighbor in adj[curr]:
            if visited_order[neighbor] == 0:
                order += 1
                visited_order[neighbor] = order
                queue.append(neighbor)

    # 결과 출력
    sys.stdout.write('\n'.join(map(str, visited_order[1:])) + '\n')

if __name__ == "__main__":
    solve()