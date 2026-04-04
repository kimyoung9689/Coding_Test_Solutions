import sys

# 재귀 깊이 제한 해제
sys.setrecursionlimit(10**6)

def solve() -> None:
    # 입력 처리
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    m: int = int(input_data[0])
    n: int = int(input_data[1])
    grid: list[list[int]] = []
    
    idx = 2
    for _ in range(m):
        grid.append([int(x) for x in input_data[idx : idx + n]])
        idx += n

    # DP 테이블 초기화 (-1은 미방문)
    dp: list[list[int]] = [[-1] * n for _ in range(m)]

    # 이동 방향 (상, 하, 좌, 우)
    dy: list[int] = [-1, 1, 0, 0]
    dx: list[int] = [0, 0, -1, 1]

    def dfs(y: int, x: int) -> int:
        # 목적지에 도착한 경우 경로 1개 발견
        if y == m - 1 and x == n - 1:
            return 1

        # 이미 계산한 적이 있다면 그 값 바로 사용
        if dp[y][x] != -1:
            return dp[y][x]

        # 방문 표시 (0으로 초기화 후 탐색 시작)
        dp[y][x] = 0

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]

            # 지도 범위 내에 있고, 높이가 더 낮은 곳인지 확인
            if 0 <= ny < m and 0 <= nx < n:
                if grid[ny][nx] < grid[y][x]:
                    dp[y][x] += dfs(ny, nx)

        return dp[y][x]

    # 결과 출력
    print(dfs(0, 0))

if __name__ == "__main__":
    solve()