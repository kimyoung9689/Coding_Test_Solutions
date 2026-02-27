import sys
from collections import deque
from typing import List, Deque, Tuple


def solve() -> None:
    # 입력 처리 (M: 가로, N: 세로, H: 높이)
    m, n, h = map(int, sys.stdin.readline().split())

    # 3차원 창고 배열 생성 (h, n, m 순서)
    graph: List[List[List[int]]] = []
    queue: Deque[Tuple[int, int, int]] = deque()

    for i in range(h):
        layer: List[List[int]] = []
        for j in range(n):
            row: List[int] = list(map(int, sys.stdin.readline().split()))
            for k in range(m):
                # 익은 토마토(1) 위치를 큐에 미리 저장
                if row[k] == 1:
                    queue.append((i, j, k))
            layer.append(row)
        graph.append(layer)

    # 6방향 탐색 (위, 아래, 앞, 뒤, 좌, 우)
    dz: List[int] = [1, -1, 0, 0, 0, 0]
    dy: List[int] = [0, 0, 1, -1, 0, 0]
    dx: List[int] = [0, 0, 0, 0, 1, -1]

    while queue:
        z, y, x = queue.popleft()

        for i in range(6):
            nz: int = z + dz[i]
            ny: int = y + dy[i]
            nx: int = x + dx[i]

            # 창고 범위를 벗어나지 않고, 익지 않은 토마토(0)인 경우
            if 0 <= nz < h and 0 <= ny < n and 0 <= nx < m:
                if graph[nz][ny][nx] == 0:
                    # 토마토를 익히고 날짜를 기록 (이전 값 + 1)
                    graph[nz][ny][nx] = graph[z][y][x] + 1
                    queue.append((nz, ny, nx))

    # 결과 계산
    max_days: int = 0
    for layer in graph:
        for row in layer:
            for cell in row:
                # 익지 않은 토마토가 남아있으면 -1 출력 후 종료
                if cell == 0:
                    print(-1)
                    return
                max_days = max(max_days, cell)

    # 처음에 1부터 시작했으므로 1을 빼줌
    # 모든 토마토가 이미 익어있었다면 max_days는 1이므로 0이 출력됨
    print(max_days - 1)


if __name__ == "__main__":
    solve()