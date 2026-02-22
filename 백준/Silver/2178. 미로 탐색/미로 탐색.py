import sys
from collections import deque
from typing import List, Tuple


def solve() -> None:
    # 입력 처리
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n: int = int(input_data[0])
    m: int = int(input_data[1])
    maze_str: List[str] = input_data[2:]

    # 미로를 정수 리스트로 변환
    maze: List[List[int]] = []
    for row in maze_str:
        maze.append([int(char) for char in row])

    # BFS를 위한 큐와 방향 설정
    queue: deque[Tuple[int, int]] = deque([(0, 0)])
    dx: List[int] = [-1, 1, 0, 0]
    dy: List[int] = [0, 0, -1, 1]

    while queue:
        x, y = queue.popleft()

        # 네 방향 탐색
        for i in range(4):
            nx: int = x + dx[i]
            ny: int = y + dy[i]

            # 미로 범위 내에 있고, 이동 가능한 칸(1)인 경우
            if 0 <= nx < n and 0 <= ny < m:
                if maze[nx][ny] == 1:
                    # 이전 칸의 거리 + 1을 저장하고 큐에 삽입
                    maze[nx][ny] = maze[x][y] + 1
                    queue.append((nx, ny))

    # (N, M) 위치의 최단 거리 출력
    print(maze[n - 1][m - 1])


if __name__ == "__main__":
    solve()