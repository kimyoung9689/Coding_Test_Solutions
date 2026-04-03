import sys
from typing import List


def solve() -> None:
    # 모든 입력을 한 번에 읽어와 처리
    input_data: List[str] = sys.stdin.read().split()
    if not input_data:
        return

    n: int = int(input_data[0])
    
    # 행렬의 차원을 중복 없이 저장 (N개 행렬이면 N+1개의 차원 정보가 필요)
    # 예: (5x3), (3x2), (2x6) -> [5, 3, 2, 6]
    dims: List[int] = []
    dims.append(int(input_data[1]))  # 첫 번째 행렬의 행
    for i in range(1, n + 1):
        dims.append(int(input_data[i * 2]))  # 각 행렬의 열 정보들

    # DP 테이블 초기화
    dp: List[List[int]] = [[0] * n for _ in range(n)]

    # dist: 곱할 행렬의 개수 차이 (범위)
    for dist in range(1, n):
        for i in range(n - dist):
            j: int = i + dist
            
            # i부터 j까지의 최소 곱셈 횟수를 구함
            # k=i일 때의 값을 초기값으로 설정하여 루프 내 조건문 감소
            min_val: int = (
                dp[i][i] + dp[i + 1][j] + (dims[i] * dims[i + 1] * dims[j + 1])
            )
            
            for k in range(i + 1, j):
                current_val: int = (
                    dp[i][k] + dp[k + 1][j] + (dims[i] * dims[k + 1] * dims[j + 1])
                )
                if min_val > current_val:
                    min_val = current_val
            
            dp[i][j] = min_val

    sys.stdout.write(str(dp[0][n - 1]) + '\n')


if __name__ == "__main__":
    solve()