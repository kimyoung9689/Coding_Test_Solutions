import sys
from collections import deque
from typing import List, Tuple


def solve() -> None:
    # 입력 받기
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n: int = int(input_data[0])
    m: int = int(input_data[1])
    grid: List[str] = input_data[2:]

    # visited[x][y][0]: 벽 안 부수고 방문, visited[x][y][1]: 벽 부수고 방문
    # 초기값 -1은 방문하지 않음을 의미
    visited: List[List[List[int]]] = [
        [[-1] * 2 for _ in range(m)] for _ in range(n)
    ]

    # BFS 시작 (x, y, 벽 부쉈는지 여부)
    queue: deque = deque([(0, 0, 0)])
    visited[0][0][0] = 1

    dx: Tuple[int, ...] = (1, -1, 0, 0)
    dy: Tuple[int, ...] = (0, 0, 1, -1)

    while queue:
        x, y, broken = queue.popleft()

        # 목적지 도착 시 거리 반환
        if x == n - 1 and y == m - 1:
            print(visited[x][y][broken])
            return

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                # 1. 다음 칸이 이동 가능한 길(0)인 경우
                if grid[nx][ny] == '0' and visited[nx][ny][broken] == -1:
                    visited[nx][ny][broken] = visited[x][y][broken] + 1
                    queue.append((nx, ny, broken))
                
                # 2. 다음 칸이 벽(1)이고 아직 벽을 부순 적이 없는 경우
                elif grid[nx][ny] == '1' and broken == 0:
                    if visited[nx][ny][1] == -1:
                        visited[nx][ny][1] = visited[x][y][0] + 1
                        queue.append((nx, ny, 1))

    # 도달할 수 없는 경우
    print(-1)


if __name__ == "__main__":
    solve()