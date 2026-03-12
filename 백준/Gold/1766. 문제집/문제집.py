import heapq
import sys
from typing import List


def solve() -> None:
    # 빠른 입력을 위해 stdin 사용
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n: int = int(input_data[0])  # 문제의 수
    m: int = int(input_data[1])  # 정보의 개수

    # 각 문제의 진입 차수(나보다 먼저 풀어야 하는 문제의 개수)
    in_degree: List[int] = [0] * (n + 1)
    # 각 문제의 후속 문제 리스트
    graph: List[List[int]] = [[] for _ in range(n + 1)]

    idx = 2
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        graph[u].append(v)
        in_degree[v] += 1
        idx += 2

    # 진입 차수가 0인(지금 바로 풀 수 있는) 문제를 담을 우선순위 큐
    # 파이썬의 heapq는 최소 힙이므로 작은 번호부터 나옴
    queue: List[int] = []
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            heapq.heappush(queue, i)

    result: List[int] = []

    while queue:
        # 현재 풀 수 있는 문제 중 가장 번호가 작은 것 선택
        current = heapq.heappop(queue)
        result.append(current)

        # 해당 문제를 풀었으니 연결된 문제들의 진입 차수 감소
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            # 새롭게 풀 수 있게 된 문제가 있다면 큐에 삽입
            if in_degree[neighbor] == 0:
                heapq.heappush(queue, neighbor)

    # 결과 출력
    print(*(result))


if __name__ == "__main__":
    solve()