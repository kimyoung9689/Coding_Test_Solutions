import sys
from collections import deque
from typing import List, Deque


def solve() -> None:
    # 빠른 입력을 위해 사용해
    input_data: List[str] = sys.stdin.read().split()
    if not input_data:
        return

    n: int = int(input_data[0])  # 정점의 수
    m: int = int(input_data[1])  # 간선의 수
    r: int = int(input_data[2])  # 시작 정점

    # 그래프 연결 정보 만들기
    graph: List[List[int]] = [[] for _ in range(n + 1)]
    idx: int = 3
    for _ in range(m):
        u: int = int(input_data[idx])
        v: int = int(input_data[idx + 1])
        graph[u].append(v)
        graph[v].append(u)
        idx += 2

    # 1. 인접 정점을 오름차순으로 방문하기 위해 정렬
    for i in range(1, n + 1):
        graph[i].sort()

    # 방문 순서를 기록할 리스트 (0으로 초기화)
    visited_order: List[int] = [0] * (n + 1)
    order: int = 1

    # 2. BFS 알고리즘 시작
    queue: Deque[int] = deque([r])
    visited_order[r] = order  # 시작 정점 방문 표시

    while queue:
        u = queue.popleft()

        for v in graph[u]:
            if visited_order[v] == 0:  # 아직 방문 안 했다면
                order += 1
                visited_order[v] = order
                queue.append(v)

    # 3. 결과 출력
    sys.stdout.write('\n'.join(map(str, visited_order[1:])) + '\n')


if __name__ == "__main__":
    solve()