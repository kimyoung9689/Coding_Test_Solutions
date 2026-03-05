import sys
from collections import deque
from typing import List


def solve() -> None:
    # 빠른 입력을 위해 sys.stdin.read 사용
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n: int = int(input_data[0])  # 학생 수
    m: int = int(input_data[1])  # 비교 횟수

    # 각 학생의 진입 차수(나보다 앞에 서야 할 사람 수)
    in_degree: List[int] = [0] * (n + 1)
    # 각 학생 뒤에 서야 할 학생들 목록
    graph: List[List[int]] = [[] for _ in range(n + 1)]

    idx: int = 2
    for _ in range(m):
        a: int = int(input_data[idx])
        b: int = int(input_data[idx + 1])
        graph[a].append(b)
        in_degree[b] += 1
        idx += 2

    # 위상 정렬 시작
    result: List[int] = []
    queue: deque[int] = deque()

    # 1. 앞에 아무도 없어도 되는 학생들을 먼저 큐에 넣음
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            queue.append(i)

    # 2. 큐가 빌 때까지 반복
    while queue:
        current: int = queue.popleft()
        result.append(current)

        # 현재 학생 뒤에 서야 했던 학생들의 진입 차수 감소
        for next_student in graph[current]:
            in_degree[next_student] -= 1
            # 만약 이제 앞에 아무도 없다면 큐에 추가
            if in_degree[next_student] == 0:
                queue.append(next_student)

    # 결과 출력
    print(*(result))


if __name__ == "__main__":
    solve()