import sys
from collections import deque
from typing import List, Tuple


def solve() -> None:
    """
    나이트의 이동 최소 횟수를 구하는 메인 함수
    """
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    idx = 0
    test_cases = int(input_data[idx])
    idx += 1

    # 나이트가 이동할 수 있는 8가지 방향
    dy: List[int] = [-2, -1, 1, 2, 2, 1, -1, -2]
    dx: List[int] = [1, 2, 2, 1, -1, -2, -2, -1]

    results: List[str] = []

    for _ in range(test_cases):
        l: int = int(input_data[idx])
        start_y: int = int(input_data[idx + 1])
        start_x: int = int(input_data[idx + 2])
        target_y: int = int(input_data[idx + 3])
        target_x: int = int(input_data[idx + 4])
        idx += 5

        # 이미 목표 지점에 있는 경우
        if start_y == target_y and start_x == target_x:
            results.append("0")
            continue

        # BFS를 위한 큐와 방문 확인 및 거리 저장용 배열
        visited: List[List[int]] = [[-1] * l for _ in range(l)]
        queue: deque[Tuple[int, int]] = deque([(start_y, start_x)])
        visited[start_y][start_x] = 0

        found: bool = False
        while queue:
            y, x = queue.popleft()

            # 현재 위치에서 나이트가 이동할 수 있는 모든 칸 확인
            for i in range(8):
                ny: int = y + dy[i]
                nx: int = x + dx[i]

                # 체스판 내부이고 아직 방문하지 않았을 때만 이동
                if 0 <= ny < l and 0 <= nx < l and visited[ny][nx] == -1:
                    visited[ny][nx] = visited[y][x] + 1
                    
                    # 목표 지점에 도달하면 기록하고 중단
                    if ny == target_y and nx == target_x:
                        results.append(str(visited[ny][nx]))
                        found = True
                        break
                    
                    queue.append((ny, nx))
            
            if found:
                break

    sys.stdout.write("\n".join(results) + "\n")


if __name__ == "__main__":
    solve()