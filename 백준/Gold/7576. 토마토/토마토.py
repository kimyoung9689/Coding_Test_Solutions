import sys
from collections import deque
from typing import List, Deque, Tuple


def solve() -> None:
    # 입력 속도를 위해 sys.stdin.read 사용
    input_data: List[str] = sys.stdin.read().split()
    if not input_data:
        return

    m: int = int(input_data[0])  # 가로
    n: int = int(input_data[1])  # 세로
    
    # 격자판(창고) 만들기
    grid: List[List[int]] = []
    queue: Deque[Tuple[int, int]] = deque()
    
    idx: int = 2
    for r in range(n):
        row: List[int] = []
        for c in range(m):
            val: int = int(input_data[idx])
            row.append(val)
            # 익은 토마토는 시작점이므로 큐에 추가
            if val == 1:
                queue.append((r, c))
            idx += 1
        grid.append(row)

    # 상하좌우 이동을 위한 방향 벡터
    dr: List[int] = [-1, 1, 0, 0]
    dc: List[int] = [0, 0, -1, 1]

    max_days: int = 0

    # BFS 시작
    while queue:
        curr_r, curr_c = queue.popleft()

        for i in range(4):
            nr: int = curr_r + dr[i]
            nc: int = curr_c + dc[i]

            # 창고 범위 안이고, 익지 않은 토마토(0)인 경우
            if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 0:
                # 익게 만들고 날짜 기록 (이전 값 + 1)
                grid[nr][nc] = grid[curr_r][curr_c] + 1
                queue.append((nr, nc))
    
    # 결과 확인
    for row in grid:
        for cell in row:
            if cell == 0:
                # 익지 않은 토마토가 남아있다면 -1
                print(-1)
                return
            max_days = max(max_days, cell)

    # 처음에 1부터 시작했으므로 결과값에서 1을 빼줌
    # (모두 익어있었다면 1-1=0이 출력됨)
    print(max_days - 1)


if __name__ == "__main__":
    solve()